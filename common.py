__author__ = 'ashwin'
import os
import requests
import json
import numpy as np
import pylab as pl
env=os.environ.get('ENVIRONMENT', 'pilot')

if env is "prod":
    url_appender="dice.com"
else:
    url_appender="dicepilot.com"
