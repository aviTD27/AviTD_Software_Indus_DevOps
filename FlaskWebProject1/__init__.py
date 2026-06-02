"""
The flask application package.
"""

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

import FlaskWebProject1.views
