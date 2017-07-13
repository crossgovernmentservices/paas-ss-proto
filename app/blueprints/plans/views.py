from flask import (
  render_template,
  Blueprint,
  current_app,
  request)

import json
import os

plans = Blueprint('plans', __name__, url_prefix='/plans')

@plans.route('/')
def index():
  return render_template('plans-index.html')

@plans.route('/table-v1')
def table_v1():
  pathtodata = 'app/data/plans.json'
  if os.path.isfile( pathtodata ):
    with open( pathtodata ) as data_file:
      data = json.load( data_file )
  return render_template('plans-table.html', plans=data['plans'])

@plans.route('/table-v2')
def table_v2():
  pathtodata = 'app/data/plans.json'
  if os.path.isfile( pathtodata ):
    with open( pathtodata ) as data_file:
      data = json.load( data_file )
  return render_template('plans-table-detailed.html', plans=data['plans'])

@plans.route('/cards-v1')
def cards_v1():
  pathtodata = 'app/data/plans.json'
  if os.path.isfile( pathtodata ):
    with open( pathtodata ) as data_file:
      data = json.load( data_file )
  return render_template('plans-summary-card.html', plans=data['plans'])

@plans.route('/cards-detailed')
def cards_detailed():
  pathtodata = 'app/data/plans.json'
  if os.path.isfile( pathtodata ):
    with open( pathtodata ) as data_file:
      data = json.load( data_file )
  return render_template('plans-summary-card-detailed.html', plans=data['plans'])

@plans.route('/cards-alternative')
def cards_alternative():
  pathtodata = 'app/data/plans.json'
  if os.path.isfile( pathtodata ):
    with open( pathtodata ) as data_file:
      data = json.load( data_file )
  return render_template('plans-summary-card-alternative.html', plans=data['plans'])

@plans.route('/price-breakdown')
def price_breakdown():
  pathtodata = 'app/data/price-breakdown.json'
  referrer = request.referrer
  if os.path.isfile( pathtodata ):
    with open( pathtodata ) as data_file:
      data = json.load( data_file )
  return render_template('plans-price-breakdown.html', data=data, referrer=referrer)
