from django.shortcuts import render, render_to_response
from function.db import SqlServerDB
# Create your views here.
def test_db(request):
    db = SqlServerDB(host = '127.0.0.1',port = '1443',user = '',password = '',db = 'django',charset="utf8")
    return render_to_response('article_list.html', {})

