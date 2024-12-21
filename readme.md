# ChatDB: AI-Powered Database Assistant 

**ChatDB** is an AI-powered web application that allows users to interact with SQL databases in natural language. Powered by **LangChain** and **Groq API**, this application simplifies querying and managing SQL databases by leveraging the latest advancements in generative AI.

---

## Features

- **Natural Language Interaction**: Query your database by simply typing your questions in plain English.
- **Database Connection**: Easily connect to MySQL databases with a user-friendly interface.
- **AI Assistance**: Powered by Groq's Llama3-8b-8192 model for intelligent and accurate query generation.
- **Chat History**: View and manage your past conversations for better query tracking.
- **Error Handling**: Provides feedback for invalid queries or connection errors.
- **Clear Chat**: Quickly reset and start a fresh conversation.
- **Responsive UI**: User-friendly interface with seamless navigation between pages.

---

## Tech Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Database**: MySQL
- **AI**: LangChain, Groq API, Llama3-8b-8192
---

## Setup and Installation

### Prerequisites
- Python 3.10+
- MySQL Server
- Groq API Key

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/muhammadaman04/AI-Powered-Database-Assistant-Flask-WebApp
   cd ChatDB
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Run the application**:
   ```bash
   flask run
   ```

6. Open the app in your browser

---

## Usage

### Step 1: Connect to a Database
- Navigate to `/db_connect` to enter your database connection details (host, user, password, database name).

### Step 2: Start Chatting
- Interact with your database through natural language queries on the `/chat` page.
- Example queries:
  - "Show me all the records in the `customers` table."
  - "How many orders were placed in December?"

### Step 3: Clear Chat History
- Use the **Clear Chat** button to reset the conversation.

---

---

## Future Enhancements

- Support for other SQL databases (PostgreSQL, SQLite).
- Improved query validation and suggestions.
- Advanced analytics and visualization of query results.
- Role-based access control for database management.

---

**ChatDB: Let AI simplify your database interactions.** 