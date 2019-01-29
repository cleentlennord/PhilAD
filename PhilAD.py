from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from nltk.tag import CRFTagger

import pycrfsuite
import traceback

app = Flask(__name__)

ct_reloaded = CRFTagger()
ct_reloaded.set_model_file('data_test.model')

app.config['SECRET_KEY'] = '601bbfb9d4c8e0a4a0a66d8f9b2f79cd'

#dropdown#
@app.route('/dropdown', methods=['POST'])
def dropdown():
    data = pd.read_excel('data_lookup.xlsx')
    data.columns
    data = data[['barangay', 'city']]
    lookup = []

        for (i, row) in data.iterrows():
            item = []

            for (j, column) in row.iteritems():
                item.append((str(column), j))

            lookup.append(item)

    return lookup;
##forms##
class Address(FlaskForm):
    address = StringField('Input Address')

@app.route('/predict', methods=['POST'])
def predict():
    if ct_reloaded:
        try:
            data = request.form
            norm_input = list(map(str.strip, data['address'].split(',')))
            prediction = ct_reloaded.tag(norm_input)
            return jsonify({'prediction': {tag: token for (token, tag) in prediction}})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return 500, 'Model Not Found'

##start website##
@app.route("/", methods = ['GET', 'POST'])
def home():
    form = Address()
    return render_template('PhilADhome.html', title='PhilaD', form=form)

#initialize app from cmd
if __name__ == '__main__':
    app.run(debug=True)
