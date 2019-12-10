#!/usr/bin/env python3

import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/flask-app/')

from app import app as application
application.secret_key ='it393_flask_app.secret_key'
