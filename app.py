from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def web():
    return render_template('/webpage.html')\
    
@app.route('/webpage')
def page():
    return render_template('/webpage.html')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/vinumon')
def vin():
    return render_template('/vinumon.html')

@app.route('/about')
def about():
    return render_template('/about.html')


if(__name__=="__main__"):
    app.run(port=4000)