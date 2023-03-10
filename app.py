from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from os import os

#port = int(os.environ.get('PORT', 5000))
# create the extension
db = SQLAlchemy()
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class link_list (db.Model):
    link_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.title} - {self.link}"

with app.app_context():
    db.create_all()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        title = request.form['title']
        category = request.form['category']
        link = request.form['link']

        link_inst = link_list(title = title, category = category, link = link)
        db.session.add(link_inst)
        db.session.commit()
    all_links = link_list.query.all()
    print(all_links)
    return render_template('index.html', all_links = all_links)
    #return 'Hello, World!'



@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        link = db.get_or_404(link_list, id)
        link.title = request.form['title']
        link.category = request.form['category']
        link.link = request.form['link']
        db.session.commit()
    #if request.method == 'POST':
    #    print(id)
        return redirect("/")
    link = db.get_or_404(link_list, id)
    return render_template('update.html', link = link)

@app.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    link = db.get_or_404(link_list, id)
    #print(id)
    db.session.delete(link)
    db.session.commit()
    #if request.method == 'POST':
    #    print(id)
    return redirect("/")

if __name__ =="__main__":
    app.run(debug = True, host='0.0.0.0', port= 5000)