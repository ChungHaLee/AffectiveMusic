import numpy as np
import librosa

def Music_Name_To_Path(Music_array):    #음악 이름 array를 path로 바꿔주는 함수입니다. 음악 파일, 확장자명이 변경되면 수정이 필요
    path = "music/"
    file_type = ".mp3"
    for i in range(len(Music_array)):
        Music_array[i] = path + Music_array[i] + file_type
    return Music_array


def amplitude_maker(file, fps):     #fps 값으로 Amplitude haptic pattern으로 변형하는 함수
    sig, _ = librosa.load(file, sr=22050)
    plat_num = int(22050/fps)       #Fps가 높아도 loop 속도에 맞춰서 출력되기 때문에 높아도 상관은 없지만 무거워지니 일단 10으로
    sig_1 = np.zeros(int(len(sig) / plat_num))
    for i_1 in range(len(sig_1)):
        sig_1[i_1] = abs(sig[i_1 * plat_num])
    sig_1 = sig_1 / np.max(sig_1) * 255
    return sig_1.astype(np.int64)



# 감정 키워드 함수입니다. 늘어나면 같이 추가하면 됩니다.
Emotion_array = ["amazement",
                 "tenderness",
                 "nostalgia",
                 "calmness",
                 "power",
                 "jpyful",
                 "tension",
                 "sadness"]

# 음악 이름입니다, 만약 haptic array 저장 코드가 주석으로 되어 있으면 음악 이름 변경 후, 밑의 코드를 실행해야합니다.
Music_array   = ["amazement",
                 "tenderness",
                 "nostalgia",
                 "calmness",
                 "power",
                 "joyful",
                 "tension",
                 "sadness"]

# 간단히 array를 가져올 수 있도록 변형하는 코드입니다.
Music_array = Music_Name_To_Path(Music_array)
Emotion_array = np.array(Emotion_array)
Music_array = np.array(Music_array)

# 음악을 햅틱으로 변형하여 저장하는 코드입니다.
# 음악이 바뀌면 다시 haptic pattern을 저장해야하기 때문에 꼭 한번은 실행해야합니다.
# 주석처리를 안해도 main 코드 실행에는 문제가 없지만, main 실행에 memory랑 시간 낭비가 심할 수 있습니다.

"""haptic_array = []
for i in Music_array:
    haptic_array.append(amplitude_maker(i, 10))
haptic_array = np.array(haptic_array)
np.save("haptic_array", haptic_array)
"""
