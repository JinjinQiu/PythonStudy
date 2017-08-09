#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 23:18:55 2017

@author: ninaqiu
"""

import sqlite3
import urllib2, cookoelib
import time
from datetime import datetime

conn = sqlite3.connect('sample.db')
c = conn.cursor

c.execute('CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH )')

