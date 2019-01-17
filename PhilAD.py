from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
app = Flask(__name__)

app.config['SECRET_KEY'] = '601bbfb9d4c8e0a4a0a66d8f9b2f79cd'

##forms##
class Address(FlaskForm):
    address = StringField('Input Address', validators = [DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Submit')



##start website##
@app.route("/", methods = ['GET', 'POST'])
def home():
    form = Address()
    return render_template('PhilADhome.html', title='PhilaD', form=form)



#initialize app from cmd
if __name__ == '__main__':
    app.run(debug=True)
