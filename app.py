from calendar import c
from math import atan2
from os import curdir
from xmlrpc.server import list_public_methods
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "ZaysuJr Apenas"


DB_HOST = 'localhost' #CONFIGURAÇÃO DO BANCO DE DADOS
DB_NOME = 'football' #CONFIGURAÇÃO DO BANCO DE DADOS
DB_USER = 'postgres' #CONFIGURAÇÃO DO BANCO DE DADOS
DB_PASS = 'rootpost' #CONFIGURAÇÃO DO BANCO DE DADOS

conn = psycopg2.connect(host=DB_HOST, database=DB_NOME, user=DB_USER, password=DB_PASS)

@app.route('/')
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM cadtimes"
    cur.execute(s) #executa o SQL
    list_times = cur.fetchall() #retorna todos os registros
    return render_template('index.html', list_times=list_times)

@app.route('/cadtime', methods=['POST'])
def cadastro_time():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        nome = request.form['nome']
        gk = request.form['gk']
        lte = request.form['lte']
        zag1 = request.form['zag1']
        zag2 = request.form['zag2']
        ltd = request.form['ltd']
        mei1 = request.form['mei1']
        mei2 = request.form['mei2']
        mei3 = request.form['mei3']
        ata1 = request.form['ata1'] 
        ata2 = request.form['ata2']
        ata3 = request.form['ata3'] 
        cur.execute("INSERT INTO cadtimes (nome, gk, lte, zag1, zag2, ltd, mei1, mei2, mei3, ata1, ata2, ata3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, gk, lte, zag1, zag2, ltd, mei1, mei2, mei3, ata1, ata2, ata3))
        conn.commit()
        flash('Time cadastrado com sucesso!')
        return redirect(url_for('index'))
    
@app.route('/cadtime2')
def cadastro_time2():            
    return render_template('cadastro_time.html')

@app.route('/cadraking')
def ver_ranking():
    return render_template('ranking.html')

@app.route('/cadresult')
def cadastro_resultado():
    return render_template('castrar_result_final.html')

@app.route('/cadcompeticao')
def cadastro_competicao():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM cadtimes"
    cur.execute(s) #executa o SQL
    list_times = cur.fetchall() #retorna todos os registros
    return render_template('cadastro_competicao.html' , list_times=list_times)

@app.route('/cadcompeticao2', methods=['POST'])
def cada_competicao2():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM cadtimes"
    if request.method == 'POST':
        clube = request.form['clube']
        localidade = request.form['localidade']
        tempo = request.form['tempo']
        cur.execute("INSERT INTO partidas (clube, localidade, tempo) VALUES (%s, %s, %s )", (clube, localidade, tempo))
        conn.commit()
        return redirect(url_for('index'))
    
@app.route('/cadresult2')
def cadastro_resultado2():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM partidas"
    cur.execute(s) #executa o SQL
    list_times = cur.fetchall() #retorna todos os registros
    return render_template('castrar_result_final.html' , list_times=list_times)
 
@app.route('/cadresult3', methods=['POST'])
def cadastro_resultado3():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        time1 = request.form['time1']
        time2 = request.form['time2']
        cur.execute(s) #executa o SQL
        list_times2 = cur.fetchall()
        cur.execute("INSERT INTO partidas2 (time1, time2) VALUES (%s, %s )", (time1, time2))
        s = "SELECT * FROM partidas2"
        return redirect(url_for('cadastro_resultado2' , list_times2=list_times2))
 
if __name__ == "__main__":
    app.run(debug=True)