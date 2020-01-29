from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Curriculum
import pymysql

def index1(request):
    return HttpResponse('<h1>Index1</h1>')

def index2(request):
    return HttpResponse('<h1>Hi</h1>')
def main(request):
    list = Curriculum.objects.all()
    html = ''
    for cur in list:
        html += cur.name + '<br>'

    return render(request, 'firstapp/main.html', {'list':list})

def shop(request):
    conn = pymysql.connect(
    host = 'localhost', user='root', password='1234',
    db='pythondb', charset='utf8')
    cursor = conn.cursor()
    sql = '''SELECT * FROM SHOP'''
    cursor.execute(sql)
    result = cursor.fetchall()
    # show = []
    # for row in result:
    #     show.append(row)
    conn.commit()
    cursor.close()
    conn.close()
    return render(request, 'firstapp/shop.html', {'show':result})

# def article(request):
#     return render(request, 'firstapp/article.html', {})