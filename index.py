from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Inicio')
def Inicio():
    return render_template('Inicio.html')

if __name__ =='__main__':
    app.run(debug=True)