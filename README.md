# AffectiveMusic
Toy Project for Sound Design Programming (Class 2022-1)

![스크린샷 2022-05-21 오후 5 44 42](https://user-images.githubusercontent.com/59073612/169643750-260c9ebf-9006-4f50-829a-69fb0ddc84f7.png)
## Requirements
- conda 4.10.3
- python 3.8.5
- Flask 2.0.3
- **여기에 햅틱 코드 붙이면 추가되는 라이브러리를 추가해주세요!**

## How to RUN
```
python app.py
```
**app.py** 를 실행시켜주시면 됩니다.


## from 정하...
- **app.py** 는 html 에서 받은 데이터를 가져와서 보여주는 Flask 서버입니다.
- **haptic.py** 는 햅틱 코드용으로 만든 파일입니다. 여기에 햅틱 코드 붙여주시면 됩니다!
- 감정단어마다 햅틱 패턴이 다르니 함수를 분리해서 만들고, **app.py**에다가 감정 단어에 맞는 햅틱 함수를 넣으면 될 것 같아요.
- Flask 정책 상 html 파일을 추가하려면 "꼭" templates 폴더에, css 파일이나 이미지, 오디오 등 기타 파일은 static 폴더에 저장해야 한다고 합니다. 혹시 관련 파일 추가하면 경로 확인 해주세요!
- python 파일은 그냥 현재 위치에 놔두면 됩니다.

## from 송민
- **main.py**은 **app.py**와 Haptic 디바이스 제어 코드를 Multiprocessing으로 합친 코드입니다. 그냥 바로 실행하시면 됩니다. 
- **main.py**을 실행하면, **app.py**의 코드와 디바이스 제어 코드가 동시에 실행됩니다. 다만, 두 코드의 준비 시간이 다르기 때문에, main 출력에서 Music Select Mode라는 문구가 뜨면 이후에 실행을 하면 됩니다.
- **main.py**을 실행하면 감정 선택창은 http://127.0.0.1:5000 로 접속하면 됩니다.
- **Music_Json_file.py**은 감정에 따라 선택한 음악을 변경할 경우 수정해야하는 코드입니다. 반드시 음악 추가 후, Music_array에 내용을 수정하시길 바랍니다. 
- **haptic_array.npy**는 음악을 햅틱 패턴으로 바꿔 저장한 코드입니다. **main.py** 실행 시간을 단축하기 위해 저장한 내용이니 음악 변경 이후, **Music_Json_file.py**에서 새롭게 저장할 수 있습니다.
