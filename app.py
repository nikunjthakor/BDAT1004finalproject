from flask import Flask, jsonify, request, render_template 
import requests as re
import json

app = Flask(__name__,template_folder='Templates')

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/details', methods=['GET'])
def details():
    req = re.get('https://api.coinlore.net/api/tickers/')
    data = json.loads(req.content)
    return render_template('table.html', data=data['data'])

@app.route('/google-charts/pie-chart') 
def google_pie_chart(): 
    req = re.get('https://api.coinlore.net/api/tickers/')
    data = json.loads(req.content)    
    return render_template('pie-chart.html', data=data['data'])

if __name__ == '__main__':
    app.run()
