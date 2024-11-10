from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class DBConnectForm(FlaskForm):
    mysql_host = StringField('MySQL Host', validators=[DataRequired()], render_kw={"placeholder": "e.g., localhost"})
    mysql_user = StringField('MySQL User', validators=[DataRequired()], render_kw={"placeholder": "e.g., root"})
    mysql_password = PasswordField('MySQL Password', validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})
    mysql_db = StringField('MySQL Database', validators=[DataRequired()], render_kw={"placeholder": "e.g., mydatabase"})
    submit = SubmitField('Connect to Database')
