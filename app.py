from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadtime')
def cadastro_time():
    return render_template('cadastro_time.html')

@app.route('/cadraking')
def ver_ranking():
    return render_template('ranking.html')

@app.route('/cadresult')
def cadastro_resultado():
    return render_template('cadastro_resultado.html')

@app.route('/cadcompeticao')
def cadastro_competicao():
    return render_template('cadastro_competicao.html')
    
    
if __name__ == "__main__":
    app.run(debug=True)