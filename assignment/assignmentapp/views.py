from django.shortcuts import render
import MySQLdb

# Create your views here.


def list_view(request):
    conn = MySQLdb.connect(
        user="root",
        password="",
        host="localhost",
        db="lampHomework_nakazawalb"
    )

    # カーソルの取得
    cur = conn.cursor()

    # SQL実行
    # selfIntroductionテーブルから全レコード取り出す
    sql = "SELECT * from selfIntroduction"
    cur.execute(sql)

    # 実行結果の取得
    rows = cur.fetchall()
    cur.close
    conn.close

    return render(request, 'assignmentapp/list_view.html',context={'data':rows})
