import mysql.connector
import click

from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect()