from flask import Flask, render_template, redirect, url_for, request, session, flash
from forms import DBConnectForm
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from langchain_groq import ChatGroq
from langchain.agents import create_sql_agent, AgentType
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.callbacks import StreamlitCallbackHandler
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')
groq_api_key = app.config['GROQ_API_KEY']
if not groq_api_key:
    raise ValueError("Groq API key not found. Please set it in the .env file.")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", streaming=True)

def get_db():
    """Create and return a SQLDatabase instance."""
    mysql_host = session.get('mysql_host')
    mysql_user = session.get('mysql_user')
    mysql_password = session.get('mysql_password')
    mysql_db = session.get('mysql_db')
    
    if not all([mysql_host, mysql_user, mysql_password, mysql_db]):
        return None
    
    try:
        engine = create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")
        connection = engine.connect()
        connection.close()
        return SQLDatabase(engine)
    except SQLAlchemyError as e:
        flash(f"Error connecting to the database: {e}", "danger")
        return None
    
@app.route('/')
def index():
    """Landing page with a 'Try Now' button."""
    return render_template('index.html')

@app.route('/db_connect', methods=['GET', 'POST'])
def db_connect():
    """Page for collecting database connection details."""
    form = DBConnectForm()
    if form.validate_on_submit():
        # Store form data in session
        session['mysql_host'] = form.mysql_host.data
        session['mysql_user'] = form.mysql_user.data
        session['mysql_password'] = form.mysql_password.data
        session['mysql_db'] = form.mysql_db.data

        db = get_db()
        if db:
            flash("Database connected successfully!", "success")
            return redirect(url_for('chat'))
        else:
            flash("Failed to connect to the database. Please check your details.", "danger")
    
    return render_template('db_connect.html', form=form)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Chat UI where user can interact with the database."""
    if 'mysql_host' not in session:
        return redirect(url_for('db_connect')) 
    db = get_db()
    if not db:
        return redirect(url_for('db_connect'))

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True
    )

    if 'messages' not in session:
        session['messages'] = [{"role": "assistant", "content": "How can I help you with your database today?"}]
    
    generating_response = False

    if request.method == 'POST':
        user_query = request.form.get('query')
        if user_query:
            session['messages'].append({"role": "user", "content": user_query})

            session['generating_response'] = True
            session.modified = True 

            try:
                response = agent.run(user_query)
                session['messages'].append({"role": "assistant", "content": response})
                session.pop('generating_response', None)

                session.modified = True 
            except Exception as e:
                flash(f"Error processing the query: {str(e)}", "danger")

            return redirect(url_for('chat'))

    generating_response = 'generating_response' in session

    return render_template('chat.html', messages=session.get('messages', []), generating_response=generating_response)


@app.route('/clear_chat')
def clear_chat():
    """Clear chat history."""
    session.pop('messages', None)
    flash("Chat history cleared.", "info")
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(debug=True)



