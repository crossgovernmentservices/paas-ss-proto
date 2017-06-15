from flask import (
  render_template,
  Blueprint,
  current_app)

import json
import os

plans = Blueprint('plans', __name__, url_prefix='/plans')

@plans.route('/')
def index():
  return render_template('plans-index.html')
