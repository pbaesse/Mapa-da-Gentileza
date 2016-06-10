from flask import render_template, flash, redirect, session, url_for
from flask import request
from app import app
from functools import wraps
from app import db,models
from sqlalchemy import func
from .models import *

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		gentileza = models.Gentileza(descricao=request.form['descricao'],tipo=request.form['tipo'],latitude=request.form['latitude'],longitude=request.form['longitude'],nome=request.form['nome'])
		db.session.add(gentileza)
		db.session.commit()
	gentilezas = db.session.query(Gentileza).all()
	return render_template("main.html",gentilezas=gentilezas);