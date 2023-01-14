from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, json
from flask_bootstrap import Bootstrap
import pandas as pd

app = Flask(__name__)

app.config.from_object('config')

Bootstrap(app)


