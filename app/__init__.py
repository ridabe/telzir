from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, json
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap
import pandas as pd
import os

app = Flask(__name__)

app.config.from_object('config')

Bootstrap(app)
load_dotenv()



