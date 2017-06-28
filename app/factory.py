# -*- coding: utf-8 -*-
"""
Flask app factory class
"""

import os
import json

from flask import Flask, render_template, session

def create_app(config='config.py', **kwargs):
    """
    App factory function
    """

    app = Flask(__name__)
    app.config.from_pyfile(config)
    app.config.update(kwargs)

    register_blueprints(app)
    register_context_processors(app)
    register_extensions(app)

    return app

def register_blueprints(app):
    """
    Import and register blueprints
    """

    from app.blueprints.base.views import base
    app.register_blueprint(base)

    from app.blueprints.ss.views import ss
    app.register_blueprint(ss)

    from app.blueprints.docs.views import docs
    app.register_blueprint(docs)

    from app.blueprints.plans.views import plans
    app.register_blueprint(plans)

def register_context_processors(app):
    """
    Add template context variables and functions
    """

    def base_context_processor():
      return {
          'asset_path': '/static/govuk_template/assets/'}

    """
    Provide org details to all templates
    """
    def org_context_processor():
      with open('app/data/org.json') as data_file:
        org = json.load( data_file )
      return org

    app.context_processor(base_context_processor)
    app.context_processor(org_context_processor)

def register_extensions(app):
    """
    Import and register flask extensions and initialize with app object
    """

    from app.assets import assets
    assets.init_app(app)
