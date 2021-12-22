import webbrowser
import tensorflow as tf
import numpy as np
from flask import Flask, request
app = Flask(__name__)
model = tf.keras.models.load_model('save1.h5')
style = """<style>
    .footer{background-color:#D5D5D5;
        text-align:center;
        position:absolute;
        bottom:0;
        width:98%;
        }
      table{
        text-align:center;
      }</style>"""


def mkhtml(predict=""):
    html = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>따릉이 수요 에측</title>
{0}
</head><body>
    <form action="/" method="post">
      <center>
        <h2>1조 신규 대여소 설치 타당성 검증을 위한 서울시 공공 자전거 수요 예측</h2><br>
        <table border="2"  bordercolor="white" width="500px">
            <tr height="30">
                <td>유동 인구</td>
                <td><input type="number" name = "move" required></td>
              </tr>
              <tr height="40">
                  <td>지하철 역과의 거리</td>
                  <td><input type='number' name = "subway_dis" required></td>
                </tr>
                <tr height="40">
                    <td>공원의 유무</td>
                    <td><input type="radio" value="1" name = "park" required>有 &nbsp
                    <input type="radio" value="0" name = "park" required>無</td>
                  </tr>
            </table>
        <br>
        <input type="submit" value='수요 예측하기'></center> </form>
    <center>
    <br> 예측되는 따릉이 이용 수요 : {1} 이상 대여 할 것으로 예측됩니다
    </center>
<center>
<footer class="footer">
<p>광운대학교 국가기간전략훈련 빅데이터분석 및 구축을 위한 파이썬머신러닝과정</p>
<p>최세윤, 김은비, 백영서, 홍석준</p>
</footer></center></body></html>""".format(style, predict)
    return html


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 파라미터를 전달 받습니다.
        move_temp = float(request.form['move'])
        subwayDis_temp = float(request.form['subway_dis'])
        park_temp = float(request.form['park'])
        y = model.predict(np.array([[move_temp, subwayDis_temp, park_temp]]))
        out = int(y[0][0] /1000)
        out = out * 1000
        html = mkhtml(str(out))
    else:
        html = mkhtml()
    return html


if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(debug=False)
    # todo-seyun 완성시 debug=False으로 변경 필요(창이 여러개 켜짐 방지)