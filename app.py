from flask import Flask, render_template, request
from haptic import haptic_function # 햅틱 함수 바꾸면 여기도 바꾸기


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
  if request.method == 'POST':
    if request.form['word_type'] == 'dynamic':
      word = '다이나믹한'
      haptic = haptic_function()  # 감정 단어에 맞게 햅틱 함수를 다르게 하면 될듯. haptic_dynamic, haptic_sad 이런식으로...
    elif request.form['word_type'] == 'energetic':
      word = '에너제틱한'
      haptic = haptic_function()
    elif request.form['word_type'] == 'catchy':
      word = '시선을 확 끄는'
      haptic = haptic_function()
    elif request.form['word_type'] == 'relaxed':
      word = '차분한'
      haptic = haptic_function()
    elif request.form['word_type'] == 'bored':
      word = '지루한'
      haptic = haptic_function()
    elif request.form['word_type'] == 'fear':
      word = '두려운'
      haptic = haptic_function()
    elif request.form['word_type'] == 'sad':
      word = '슬픈'
      haptic = haptic_function()
    elif request.form['word_type'] == 'angry':
      word = '화나는'
      haptic = haptic_function()
    elif request.form['word_type'] == 'annoyed':
      word = '짜증나는'
      haptic = haptic_function()
    else:
      pass
  elif request.method == 'GET':
    pass
  return render_template('result.html', word=word, haptic=haptic)


if __name__ == '__main__':
  app.run(debug=True)





