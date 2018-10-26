import os

from flask import Flask
from . import db as db_access
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    # a simple page that says hello
    @app.route('/')
    def hello():
        db = db_access.get_db()
        classes = db.execute('SELECT * from classe').fetchall()
        return render_template('home.html', classes=classes)



    @app.route('/classe/<int:id>')
    def classe(id):
        db = db_access.get_db()
        eleves = db.execute(
            'SELECT * FROM eleve WHERE classe_id = ? ', (id,)).fetchall()
        return render_template('voirClasse.html', eleves=eleves, classe_id=id)




    @app.route('/inscrire', methods=('POST', 'GET'))
    def inscrire():
        db = db_access.get_db()
        if request.method == 'POST':
            nom = request.form['nom']
            prenom = request.form['prenom']
            age = request.form['age']
            classe_id = request.form['classe']
            db.execute(
                'INSERT INTO eleve (nom, prenom, age, classe_id)'
                ' VALUES (?, ?, ?, ?)',
                (nom, prenom, age, classe_id)
                    )
            db.commit()
            return redirect(url_for('hello'))
        elif request.method == 'GET':
            classes = db.execute(
                'SELECT * FROM classe').fetchall()
        return render_template('incription.html', classes=classes)



    @app.route('/modifier/<int:id>', methods=('POST', 'GET'))
    def modifier(id):
        db = db_access.get_db()
        if request.method == 'POST':
            niveau = request.form['niveau']
            designation = request.form['designation']
            capacite = request.form['capacite']
            db.execute(
                'UPDATE classe SET niveau = ?, designation = ?, capacite = ?'
                'WHERE id = ?',
                (niveau, designation, capacite, id)
            )
            db.commit()
            return redirect(url_for('classe'))
        elif request.method == 'GET':
            classe = db.execute(
                'SELECT * FROM classe WHERE id = ? ', (id,)).fetchone()
            return render_template('modifierClasse.html', classe=classe)



    @app.route('/modifier/eleve/<int:id>/<int:classe_id>', methods=('POST', 'GET'))
    def modifierEleve(id, classe_id):
        db = db_access.get_db()
        if request.method == 'POST':
            nom = request.form['nom']
            prenom = request.form['prenom']
            age = request.form['age']
            classe = request.form['classe']
            print("======================================")
            print(classe)
            print("======================================")
            db.execute(
                'UPDATE eleve SET nom = ?, prenom = ?, age = ?, classe_id = ?'
                'WHERE id = ?',
                (nom, prenom, age, classe, id)
            )
            db.commit()
            return redirect(url_for('classe', id=classe_id))            
        elif request.method == 'GET':
            eleve = db.execute(
                'SELECT * FROM eleve WHERE id = ? ', (id,)).fetchone()
            classes = db.execute(
                'SELECT * FROM classe').fetchall()
            return render_template('modifierEleve.html', eleve=eleve, classes=classes)




    @app.route('/ajouter', methods=('POST', 'GET'))
    def ajourer():
        if request.method == 'POST':
            niveau = request.form['niveau']
            designation = request.form['designation']
            capacite = request.form['capacite']
            db = db_access.get_db()
            db.execute(
                'INSERT INTO classe (niveau, designation, capacite)'
                ' VALUES (?, ?, ?)',
                (niveau, designation, capacite)
            )
            db.commit()
            return redirect(url_for('hello'))
        return render_template('ajoutClasse.html')



    @app.route('/supprimer/<int:id>', methods=('POST', 'GET'))
    def supprimer(id):
        db = db_access.get_db()
        db.execute('DELETE FROM classe WHERE id = ?', (id,))
        db.commit()
        return redirect(url_for('hello'))



    @app.route('/supprimer/eleve/<int:id>/<int:classe_id>', methods=('POST', 'GET'))
    def supprimerEleve(id, classe_id):
        db = db_access.get_db()
        db.execute('DELETE FROM eleve WHERE id = ?', (id,))
        db.commit()
        return redirect(url_for('classe', id=classe_id))

    db.init_app(app)

    return app
