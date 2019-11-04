from flask import Flask, g, request, render_template, jsonify, json
import sqlite3


app = Flask(__name__)

# data initialization
patientData=[]
with open('patients.json') as f1:
        patientData = json.load(f1)
sampleData=[]
with open('samples.json') as f2:
        sampleData = json.load(f2)
variantsData=[]
with open('variants.json') as f3:
        variantsData = json.load(f3)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

# get patients data end point
@app.route('/getPatients', methods=['GET', 'POST'])
def getPatients():
    return jsonify(result=patientData)

# get sample by patient id end point
@app.route('/getSample', methods=['GET', 'POST'])
def getSample():
    patientId = request.args.get('patientId')
    sampleList=[]
    for sample in sampleData:
        if sample['patientId']==int(patientId):
            sampleList.append(sample)

    return jsonify(result=sampleList)

# get variants by sample id end point
@app.route('/getVariants', methods=['GET', 'POST'])
def getVariants():
    sampleId = request.args.get('sampleId')
    variantList=[]

    for variant in variantsData:
        if variant['sampleId']==int(sampleId):
            variantList.append(variant)

    return jsonify(result=variantList)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
