# -*- coding: utf-8 -*-
"""day16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bw_67SXtOkeLJ6FWkdm4PY3LKTRJdyE_
"""

import pandas as pd

"""# Woking with JSON"""

pd.read_json('train.json')

pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')

"""# Working with SQL"""

!pip install mysql.connector

import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='',database='world')

df = pd.read_sql_query("SELECT * FROM countrylanguage",conn)

df
