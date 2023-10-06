from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired

class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'i can push my keys cause this is a demo'

bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get("email")

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    
    return render_template(
        'index.html', 
        form = form, 
        name = session.get('name'), 
        email = session.get('email'),
        email_error='utoronto' not in (session.get('email') or [])
    )
