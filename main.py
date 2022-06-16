import asyncio
from bleak import BleakClient
from bleak import discover
from neosensory_python import NeoDevice
import numpy as np
import time
from Music_Json_file import Emotion_array, Music_array
import librosa
import pygame
from flask import Flask, render_template, request
from multiprocessing import Process, Manager

import sys

# if sys.version_info[:2] >= (3, 7):
#     from asyncio import get_running_loop
# else:
#     from asyncio import _get_running_loop as get_running_loop


# 정하가 만든 html 코드입니다. 따로 수정은 안했지만, haptic 코드 대신에 Global 역할로 공용변수를 수정하는 코드를 넣었습니다.
# ---------------------------------------------------------------------
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

def word_name_get(app, word):
  app.word_list[0] = word

@app.route('/amazement', methods=['GET', 'POST'])
def amazement():
  if request.method == 'POST':
    if request.form['word_type'] == 'amazement':
      word = 'amazement'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('amazement.html', word=word)


@app.route('/tenderness', methods=['GET', 'POST'])
def tenderness():
  if request.method == 'POST':
    if request.form['word_type'] == 'tenderness':
      word = 'tenderness'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('tenderness.html', word=word)



@app.route('/nostalgia', methods=['GET', 'POST'])
def nostalgia():
  if request.method == 'POST':
    if request.form['word_type'] == 'nostalgia':
      word = 'nostalgia'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('nostalgia.html', word=word)



@app.route('/calmness', methods=['GET', 'POST'])
def calmness():
  if request.method == 'POST':
    if request.form['word_type'] == 'calmness':
      word = 'calmness'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('calmness.html', word=word)



@app.route('/power', methods=['GET', 'POST'])
def power():
  if request.method == 'POST':
    if request.form['word_type'] == 'power':
      word = 'power'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('power.html', word=word)


@app.route('/joyful', methods=['GET', 'POST'])
def joyful():
  if request.method == 'POST':
    if request.form['word_type'] == 'joyful':
      word = 'joyful'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('joyful.html', word=word)


@app.route('/tension', methods=['GET', 'POST'])
def tension():
  if request.method == 'POST':
    if request.form['word_type'] == 'tension':
      word = 'tension'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('tension.html', word=word)


@app.route('/sadness', methods=['GET', 'POST'])
def sadness():
  if request.method == 'POST':
    if request.form['word_type'] == 'sadness':
      word = 'sadness'
      word_name_get(app, word)
  elif request.method == 'GET':
    pass
  return render_template('sadness.html', word=word)


def app_function(word_list):    # multiprocessing 실행을 위해 임의로 설정했습니다.
    app.word_list = word_list
    app.run()

# ---------------------------------------------------------------------


# Haptic 디바이스 제어 코드입니다. 상단 코드와 동시에 processing으로 실행이 됩니다.

global Play, Music_index, Flag1_MusicReset, Flag2_MusicStart
def Emotion_Music_selecter(Music_index):    # Html에서 선택한 감정 단어에 맞는 haptic pattern을 찾아주는 함수입니다.
    global Flag1_MusicReset, Flag2_MusicStart    # 추가로 감정이 변경되었다는 신호도 체크하고 있습니다. (++ Start 버튼도 체크하고 있습니다)
    if word_list[1] == "Start":
        Flag2_MusicStart = True
    if word_list[0] != "None":
        index = np.where(Emotion_array == word_list[0])[0][0]
        if index != Music_index:
            Flag1_MusicReset = True
        return index
    else:
        return -1

def Flag_checking(Music_index):             # 음악 진행 도중에 감정을 다시 선택했는지 확인하는 코드입니다.
    return Music_index != np.where(Emotion_array == word_list[0])[0][0]

async def run(loop):        # haptic 디바이스 제어 코드입니다. async로 진행되어 디바이스 연결부터 전부 하나의 코드로 만들어져야 합니다.
    global Play, Music_index, Flag1_MusicReset, Flag2_MusicStart
    Play = False
    Music_index = -1
    Flag1_MusicReset = False
    Flag2_MusicStart = False
    fps = 10
    haptic_array = np.load("haptic_array.npy")

    #-------------------Default Setting 코드가 의도대로 진행 되도록 설정한 값이니 수정을 안하는게 좋습니다.

    buzz_addr = "E5:72:19:73:4A:3B"
    devices = await discover()
    for d in devices:
        if str(d).find("Buzz") > 0:
            print("Found a Buzz! " + str(d) + "\r\nAddress substring: " + str(d)[:17])
            # set the address to a found Buzz
            buzz_addr = str(d)[:17]
    async with BleakClient(buzz_addr, loop=loop) as client:
        my_buzz = NeoDevice(client)
        await asyncio.sleep(1)
        x = await client.is_connected()
        await asyncio.sleep(1)
        await my_buzz.request_developer_authorization()
        await my_buzz.accept_developer_api_terms()
        await my_buzz.pause_device_algorithm()
        print("Bluetooth connected")
    #---------------------Bluetooth conncection
        try:
            while True:
                if Play == False:       # 음악 선택 단계임을 보여주는 코드입니다.
                    print("-----------------")
                    print("-----------------")
                    print("Music Select Mode")
                    print("-----------------")
                    print("-----------------")# 첫 코드를 실행할 경우 이 print가 실행된 이후에 음악을 골라야 원할한 진행이 됩니다.
                    while True:               # 음악이 선택되기 전까지는 이 loop에서 선택을 기다립니다.
                        Music_index = Emotion_Music_selecter(Music_index)
                        if Flag1_MusicReset:    # 음악이 선택되면 flag를 통해 인식되면
                            print("Music selected")     # 기본적인 parameter를 설정하고 loop를 빠져나갑니다.
                            Flag1_MusicReset = False
                            arr_buzz = haptic_array[Music_index]
                            print("CHeck1", arr_buzz)
                            break
                        if Flag2_MusicStart:
                            Flag2_MusicStart = False
                            Play = True
                    time.sleep(0.01)
                elif Play == True:      # 음악 실행 코드입니다.
                    print("Music Play Mode")
                    buzz_vibration_frame = [0, 0, 0, 0]
                    delay = -0.01  # 디바이스의 출력에 딜레이가 있으면 값을 추가합니다. 디바이스 출력이 늦을 수록 -값을 증가(단위: sec)
                    length = arr_buzz.shape[0]
                    Fin_check = False       # 디바이스가 종료되야하는지 체크하는 tool 입니다.
                    # -------------------------Initial Setting
                    pygame.mixer.init(44100, -16, 2, 10240)
                    pygame.mixer.music.load(Music_array[Music_index])
                    pygame.mixer.music.play()         # >> 음악 출력 코드입니다.
                    start = time.time() + delay
                    a = 0
                    while True:     # 디바이스 실행이 진행되는 코드입니다.
                            await asyncio.sleep(0.01)
                            await my_buzz.vibrate_motors(buzz_vibration_frame)  # loop 중 디바이스의 출력값을 받는 부분입니다.
                            if Fin_check:
                                print("Music Finish")
                                Play = False
                                pygame.mixer.music.stop()  # 혹시 음악이 종료되지 않을 경우, 강제로 종료합니다.
                                break
                            a = int((time.time() - start) * fps)
                            if a > length-1:    # 음악이 모두 재생되었음을 확인하는 부분입니다.
                                Fin_check = True
                            elif Flag_checking(Music_index):    # 음악을 새롭게 선택했음을 확인하는 부분입니다.
                                Flag1_MusicReset = True
                                Play = False
                                Fin_check = True
                                word_list[1] = "Stop"
                                a += 9000000    # 강제로 Timeout시키는 방식으로 종료 >> 그래야 buzz 출력을 0으로 설정 가능
                            if a > length-1:       # 디바이스의 종료 여부를 확인하고 마지막 출력이 0이 되도록 설정합니다.
                                buzz_vibration_frame = [0, 0, 0, 0]
                            else:
                                buzz_vibration_frame = [arr_buzz[a], arr_buzz[a], arr_buzz[a], arr_buzz[a]]

                            print("time:", time.time() - start, "OUTPUT:, ", buzz_vibration_frame)
        except KeyboardInterrupt:
                await my_buzz.resume_device_algorithm()
                pass

if __name__ == "__main__":
    manager = Manager()
    word_list = manager.list()
    word_list.append("None")
    word_list.append("Stop")
    proc = Process(target=app_function, args=(word_list,))
    proc.start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    proc.join()
