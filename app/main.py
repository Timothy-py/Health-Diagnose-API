from flask import Flask, request, jsonify
import os
from doctor import Doctor

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


# Route
@app.route('/', methods=['GET'])
def index():
    return jsonify({'msg': "Welcome to Health Center"})


@app.route('/diagnose', methods=['POST'])
def diagnose():
    patient_response = request.json['response']
    doctor = Doctor()
    msg = doctor.diagnose_patient(patient_response=patient_response)

    return jsonify({'msg': msg})


#     # Run server
# if __name__ == '__main__':
#     app.run(debug=True)
