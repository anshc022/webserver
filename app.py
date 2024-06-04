from flask import Flask, render_template, request, redirect, url_for
from config import app, db
from models import Entry

@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_entry = Entry(name=name, email=email)
        
        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your entry"

    return render_template('add_entry.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_entry(id):
    entry = Entry.query.get_or_404(id)
    if request.method == 'POST':
        entry.name = request.form['name']
        entry.email = request.form['email']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your entry"

    return render_template('edit_entry.html', entry=entry)

@app.route('/delete/<int:id>')
def delete_entry(id):
    entry = Entry.query.get_or_404(id)
    
    try:
        db.session.delete(entry)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue deleting your entry"


