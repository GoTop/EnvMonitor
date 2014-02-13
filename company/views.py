from django.shortcuts import render
from function.db import SqlServerDB
# Create your views here.
def test_db():
    db = SqlServerDB(host = '127.0.0.1',port = '1443',user = '',password = '',db = 'django',charset="utf8")

