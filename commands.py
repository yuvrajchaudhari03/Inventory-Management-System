import click
from flask.cli import with_appcontext

from main import db
from models import Product, Location, Productmovement, Showproducts

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
