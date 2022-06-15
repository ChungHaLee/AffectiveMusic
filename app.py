from flask import Flask, render_template, request, send_from_directory
from haptic import haptic_function # 햅틱 함수 바꾸면 여기도 바꾸기
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

# 감정단어별로 페이지를 만들어주었음 (이렇게 한 이유: 감정단어마다 나오는 노래가 다르기 때문)

@app.route('/amazement', methods=['GET', 'POST'])
def amazement():
  if request.method == 'POST':
    if request.form['word_type'] == 'amazement':
      word = 'amazement'
  elif request.method == 'GET':
    pass
  return render_template('amazement.html', word=word)


@app.route('/tenderness', methods=['GET', 'POST'])
def tenderness():
  if request.method == 'POST':
    if request.form['word_type'] == 'tenderness':
      word = 'tenderness'
  elif request.method == 'GET':
    pass
  return render_template('tenderness.html', word=word)



@app.route('/nostalgia', methods=['GET', 'POST'])
def nostalgia():
  if request.method == 'POST':
    if request.form['word_type'] == 'nostalgia':
      word = 'nostalgia'
  elif request.method == 'GET':
    pass
  return render_template('nostalgia.html', word=word)



@app.route('/calmness', methods=['GET', 'POST'])
def calmness():
  if request.method == 'POST':
    if request.form['word_type'] == 'calmness':
      word = 'calmness'
  elif request.method == 'GET':
    pass
  return render_template('calmness.html', word=word)



@app.route('/power', methods=['GET', 'POST'])
def power():
  if request.method == 'POST':
    if request.form['word_type'] == 'power':
      word = 'power'
  elif request.method == 'GET':
    pass
  return render_template('power.html', word=word)


@app.route('/joyful', methods=['GET', 'POST'])
def joyful():
  if request.method == 'POST':
    if request.form['word_type'] == 'joyful':
      word = 'joyful'
  elif request.method == 'GET':
    pass
  return render_template('joyful.html', word=word)


@app.route('/tension', methods=['GET', 'POST'])
def tension():
  if request.method == 'POST':
    if request.form['word_type'] == 'tension':
      word = 'tension'
  elif request.method == 'GET':
    pass
  return render_template('tension.html', word=word)


@app.route('/sadness', methods=['GET', 'POST'])
def sadness():
  if request.method == 'POST':
    if request.form['word_type'] == 'sadness':
      word = 'sadness'
  elif request.method == 'GET':
    pass
  return render_template('sadness.html', word=word)





if __name__ == '__main__':
  app.run(debug=True)





