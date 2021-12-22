# 최종
import webbrowser
import SineCube as SineCube
import mega_done as mega
import cgv as cgv
from flask import Flask
from datetime import datetime
app = Flask(__name__)


def call_date(info):
    return str(datetime.today().strftime("%"+info))


def list2html(lis):
    output = ""
    for i in range(5):
        output += "<br> {0}. <a href =\"{1}\">{2}</a>".format(i+1, lis[0][i], lis[1][i])
    return output


def mk_html():
    output_time = call_date("Y") + "년 " + call_date("m") + "월 " + call_date("d") + "일/ " + call_date("H") + "시 " + call_date("M") + "분 " + call_date("S") + "초"
    print("MEGA BOX 크롤링 시작")
    load_code1 = "{0}".format(list2html(mega.movie_list()))
    print("시네 큐브 크롤링 시작")
    load_code2 = "{0}".format(list2html(SineCube.movie_list()))
    print("CGV 크롤링 시작")
    load_code3 = "{0}".format(list2html(cgv.movie_list()))
    html = """<!DOCTYPE html><html><head>
            <meta charset="utf-8">
            <title>1조 크롤링 프로젝트</title>
            {0}
        </head><body>
        <div class="title_div">
        <h2>1조 크롤링 미니 프로젝트 (상영작 순위)</h2>
            <div>
                <div class="div_style"><h3>메가박스 인기순위</h3><hr>{1}</div>
                <div class="div_style"><h3>시네 큐브 인기순위</h3><hr>{2}</div>
                <div class="div_style"><h3>CGV 인기순위</h3><hr>{3}</div>
            </div>
        <br>
        크롤링된 시각: {4}<br> 
        </div>
        <footer class="footer">
            <p>광운대학교 국가기간전략훈련 빅데이터분석 및 구축을 위한 파이썬머신러닝과정</p>
            <p>최세윤, 김은비, 백영서, 홍석준</p>
        </footer></body></html>""".format(style, load_code1, load_code2, load_code3, output_time)
    return html


style = """<style>div {
        width:100%-15px;
        height: 300px;
        border: 0px solid #000;
        }
        .title_div {
        margin: 25px;
        border:0;
        }
    div.div_style {
        width: 33%;
        float: left;
        box-sizing: border-box;
        text-align: left;
        margin: 0.1%;
        padding: 20px;
        border: 2px solid #000;
        }
    h3 {
        text-align: center;
        }
    .footer{background-color:#D5D5D5;
        text-align:center;
        position:absolute;
        bottom:0;
        width:98%;
        }</style>"""


@app.route('/')
def home():
    html = mk_html()
    print("서버에 출력")
    return html


if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(debug=False)
    # todo-seyun 완성시 debug=False으로 변경 필요(창이 여러개 켜짐 방지)
