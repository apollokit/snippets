"""The main flask app."""
import glob
from os import path

import flask
from flask import (
    Flask, redirect, render_template, request, send_file)

# from vinci.db import connection


# Create the Flask app.
app = Flask('Example Server')
    
# The main UI page
@app.route('/')
def main():
    return redirect('/symbol_detail')

@app.route('/symbol_detail')
def index():
    """Detail page for a given symbol
    """
    symbol = request.args.get('symbol')

    return render_template('example.html', symbol = symbol)

@app.route('/get_symbol_plot')
def get_symbol_plot():
    """Get a path for the plot file for the symbol"""
    return send_file('<path to plot (png, jpg) file>')