import simplejson as json
from simple_salesforce import Salesforce
from flask import (Flask,redirect, render_template, request)
app = Flask(__name__)
@app.route('/app', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        urlJson={};
        sf = Salesforce(username=request.form['username'], password=request.form['password'], organizationId='')
        for a in json.loads(json.dumps(sf.query_more("/services/apexrest/ivybase/v2/URLDownload/Masters/", True)))['Data']:
            try:
                urlJson[a[1]]=json.loads(json.dumps(sf.query_more(a[1],True)))
            except  Exception as e:
                urlJson[a[1]]=str(e)
        return render_template('json.html',urlJson=enumerate(urlJson.items()))
    else:
        return render_template('app.html')  

@app.route('/sandbox', methods=['GET', 'POST'])
def sandbox():
    if request.method == 'POST':
        urlJson={};
        sf = Salesforce(domain='test',username=request.form['username'], password=request.form['password'], organizationId='')
        for a in json.loads(json.dumps(sf.query_more("/services/apexrest/ivybase/v2/URLDownload/Masters/", True)))['Data']:
            try:
                urlJson[a[1]]=json.loads(json.dumps(sf.query_more(a[1],True)))
            except  Exception as e:
                urlJson[a[1]]=str(e)
        return render_template('json.html',urlJson=enumerate(urlJson.items()))
    else:
        return render_template('app.html')  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
