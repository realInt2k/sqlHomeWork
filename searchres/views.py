from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import cx_Oracle
from elkhan.settings import DATABASES
import os
import sys
 
_user = DATABASES['default']['USER']
_password = DATABASES['default']['PASSWORD']
_dsn = DATABASES['default']['HOST']+":"+DATABASES['default']['PORT']

def sqlCount(tableName):
    res = "select count(*) from " + tableName
    return res

def sqlGet(tableName, things):
    res = "select "
    for i, item in enumerate(things):
        if(i + 1< len(things)):
            res = res + item + ", "
        else:
            res = res + item + " " 
    res = res + "from " + tableName
    return res

def connectToSqlServer():
    connection = cx_Oracle.connect(
        user=_user,
        password=_password,
        dsn=_dsn)
    cursor = connection.cursor()
    return cursor

def getInfo():
    connection = cx_Oracle.connect(
        user=_user,
        password=_password,
        dsn=_dsn)
    cursor = connection.cursor()
    movie = "SELECT * FROM movie"
    cursor.execute(movie)
    res = cursor.fetchall()
    for row in res:
        print(row)
    return res

# Create your views here.
def index(request, query='', category=''):
    print(query)
    cursor = connectToSqlServer()
    cmd = sqlGet("movie", ["movie_id", "picture"])
    cursor.execute(cmd)
    # print(request.headers.get('query')) #json

    randomThing = {'int2k': cursor.fetchall()}

    return render(request, 'templates/index2.html', randomThing)