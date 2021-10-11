from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def main_page():
    return render_template('dojo_survey.html')

@app.route('/result')
def result():
    return render_template('dojo_survey_result.html', dojo = Dojo.read_all_last())

@app.route('/compile', methods=['POST'])
def create():
    if Dojo.validate_dojo(request.form):
        Dojo.create(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/return', methods = ['POST'])
def go_back():
    return redirect('/')

@app.route('/create', methods=['POST'])
def create_dojo(): 
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.create(request.form)
    return redirect('/result')

if __name__=="__main__":
    app.run(debug=True)