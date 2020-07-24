from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Table, func, Column, Integer, ForeignKey
from sqlalchemy.sql import label
import os


from sqlalchemy.orm import relationship
import mysql.connector
from mysql.connector import Error



app = Flask(__name__)
app.secret_key = 'many random bytes'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///inventory_system'
#app.config['DATABASE_URL'] = 'mysql:///inventory_system'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)



class Product(db.Model):
    '''
    pid, p_name, quantity, location, time
    '''
    product_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(80), nullable=False)
    p_mov= db.relationship("Productmovement",backref='product1',cascade="save-update, merge, delete", lazy='dynamic')
    
class Location(db.Model):
    '''
    pid, p_name, quantity, location, time
    '''
    location_id = db.Column(db.Integer, primary_key=True)
    loc_name = db.Column(db.String(80), nullable=False)
    p_mov1 = db.relationship("Productmovement", backref='product', cascade="save-update, merge, delete", lazy='dynamic')
class Productmovement(db.Model):
    movement_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(100), nullable=True)
    from_location = db.Column(db.String(30), nullable=True)
    to_location = db.Column(db.String(30), nullable=True)
    qty = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'), nullable=False)

class Showproducts(Table):
    pid = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(100), nullable=True)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/addproducts", methods = ['POST', 'GET'])
def addproduct():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        p_name = request.form.get('p_name')
        entry = Product(p_name=p_name)
        db.session.add(entry)
        db.session.commit()
    data =Product.query.all()
    return render_template('addproducts.html',data=data)

@app.route("/productmovement",methods = ['GET'])
def productmovement():
    showproducts = Product.query.all()
    showlocation = Location.query.all()
    data2 = Productmovement.query.all()
    return render_template('productmovement.html', data=showproducts, data1=showlocation, data2=data2)

@app.route("/addproductmovement", methods=['POST','GET'])
def addproductmovement():
    if (request.method == 'POST'):
        p_name = request.form.get('p_name')
        from_location = request.form.get('fromlocation')
        to_location = request.form.get('tolocation')
        quantity = request.form.get('quantity')
        timestamp = datetime.now()
        results = Product.query.filter_by(p_name=p_name).first_or_404()
        if from_location == None:
            results1 = Location.query.filter_by(loc_name=to_location).first_or_404()
            from_location=None
        elif to_location== None:
            results1 = Location.query.filter_by(loc_name=from_location).first_or_404()
            to_location = None
        else:
            results1 = Location.query.filter_by(loc_name=to_location).first_or_404()

        product_id=results.product_id
        location_id = results1.location_id
        '''
        results2 = db.session.query(Productmovement.location_id, Productmovement.product_id,
                                    func.sum(Productmovement.qty)).group_by(Productmovement.to_location,
                                                                            Productmovement.product_id).order_by(
            Productmovement.product_id).filter_by(to_location=from_location, product_id=product_id).first()
            '''
        results2 = db.session.query(Productmovement.location_id ,Productmovement.to_location,Productmovement.product_id,func.sum(Productmovement.qty)).group_by(Productmovement.to_location, Productmovement.product_id, Productmovement.location_id).order_by(Productmovement.product_id).filter_by(to_location=from_location, product_id=product_id).first()
        if (results2[3] < int(quantity)):
            flash("Low Quantity!!")
        else:
            data = Productmovement(from_location=from_location,to_location=to_location, qty = quantity, timestamp = timestamp, product_id=product_id , location_id=location_id)
            db.session.add(data)
            db.session.commit()
    return redirect('/productmovement')

@app.route('/productmovementedit',methods=['GET','POST'])
def productmovementedit():
    if (request.method == 'POST'):
        movement_id = request.form.get('movement_id')
        from_location = request.form.get('fromloc')
        to_location = request.form.get('toloc')
        quantity = request.form.get('qty')
        if (movement_id != 0):
            results = Productmovement.query.filter_by(movement_id=movement_id).first_or_404()
            results.from_location = from_location
            results.to_location = to_location
            results.qty = quantity
            results.timestamp = datetime.now()
            flash("Data Updated Successfully")
            db.session.commit()
    return redirect('/productmovement')

@app.route("/productmovementdelete/<int:movement_id>")
def productmovementdelete(movement_id):
    flash("Record Has Been Deleted Successfully")
    results = Productmovement.query.filter_by(movement_id=movement_id).first_or_404()
    db.session.delete(results)
    db.session.commit()
    return redirect('/productmovement')

@app.route("/showproducts/", methods=['GET','POST'])
def showproduct_route():
    showproducts=Addproducts.query.all()
    return render_template('showproducts.html', data=showproducts)

@app.route("/deleteproducts")
def deleteproduct():
    showproducts = Addproducts.query.all()
    return render_template('deleteproducts.html',data=showproducts)

@app.route('/productedit',methods=['GET','POST'])
def productedit():
    if (request.method == 'POST'):
        product_id = request.form.get('product_id')
        p_name = request.form.get('p_name')
        if(product_id!=0):
            results = Product.query.filter_by(product_id=product_id).first_or_404()
            results.p_name=p_name
            flash("Data Updated Successfully")
            db.session.commit()
    return redirect('/addproducts')

@app.route('/productdelete/<int:product_id>',methods=['GET','POST'])
def productdelete(product_id):
    flash("Record Has Been Deleted Successfully")
    results = Product.query.filter_by(product_id=product_id).first_or_404()
    db.session.delete(results)
    db.session.commit()
    return redirect('/addproducts')

@app.route("/addlocation", methods = ['POST', 'GET'])
def addlocation():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        loc_name = request.form.get('loc_name')
        entry = Location(loc_name=loc_name)
        db.session.add(entry)
        db.session.commit()
    data = Location.query.all()
    return render_template('addlocation.html',data=data)

@app.route('/locationedit',methods=['GET','POST'])
def locationedit():
    if (request.method == 'POST'):
        location_id = request.form.get('location_id')
        loc_name = request.form.get('loc_name')
        if(location_id!=0):
            results = Location.query.filter_by(location_id=location_id).first_or_404()
            results.loc_name=loc_name
            flash("Data Updated Successfully")
            db.session.commit()
    return redirect('/addlocation')

@app.route('/locationdelete/<int:location_id>', methods=['GET', 'POST'])
def locationdelete(location_id):
    flash("Record Has Been Deleted Successfully")
    results = Location.query.filter_by(location_id=location_id).first_or_404()
    db.session.delete(results)
    db.session.commit()
    return redirect('/addlocation')

@app.route('/quantity')
def quantity():
    results = db.session.query(Productmovement.location_id ,Productmovement.to_location,Productmovement.product_id,func.sum(Productmovement.qty)).group_by(Productmovement.to_location, Productmovement.product_id, Productmovement.location_id).order_by(Productmovement.product_id).all()
    results3 = db.session.query(Productmovement.from_location,  Productmovement.product_id,
                               func.sum(Productmovement.qty)).group_by(Productmovement.from_location,
                                                                       Productmovement.product_id).order_by(
        Productmovement.product_id).all()


    results1=Product.query.all()
    results2 = Location.query.all()

    return render_template('quantity.html', data=results, data1=results1, data2=results2, data3=results3)
##app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
