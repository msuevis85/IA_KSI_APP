import pandas as pd
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import requests
import numpy as np
import pickle as p
import json

# Create an instance of the Flask class
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/models")
def models():
    return render_template("models.html")


if __name__ == '__main__':
    app.run(debug=True)
