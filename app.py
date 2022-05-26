from flask import Flask, render_template, request
from haptic import haptic_function # 햅틱 함수 바꾸면 여기도 바꾸기


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
  if request.method == 'POST':
    if request.form['word_type'] == 'amazement':
      word = 'Amazement'
      haptic = haptic_function()  # 감정 단어에 맞게 햅틱 함수를 다르게 하면 될듯. haptic_dynamic, haptic_sad 이런식으로...
    elif request.form['word_type'] == 'tenderness':
      word = 'Tenderness'
      haptic = haptic_function()
    elif request.form['word_type'] == 'nostalgia':
      word = 'Nostalgia'
      haptic = haptic_function()
    elif request.form['word_type'] == 'calmness':
      word = 'Calmness'
      haptic = haptic_function()
    elif request.form['word_type'] == 'power':
      word = 'Power'
      haptic = haptic_function()
    elif request.form['word_type'] == 'joyful':
      word = 'Joyful'
      haptic = haptic_function()
    elif request.form['word_type'] == 'tension':
      word = 'Tension'
      haptic = haptic_function()
    elif request.form['word_type'] == 'sadness':
      word = 'Sadness'
      haptic = haptic_function()
    else:
      pass
  elif request.method == 'GET':
    pass
  return render_template('result.html', word=word, haptic=haptic)


if __name__ == '__main__':
  app.run(debug=True)





