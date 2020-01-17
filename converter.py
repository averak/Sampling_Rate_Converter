import numpy as np
import scipy
import wave


def read_wav(file):
    ## -----*----- Wavファイルの読み込み -----*----- ##
    wf = wave.open(file)
    fs = wf.getframerate()

    # -1 ~ 1に正規化
    data = np.frombuffer(wf.readframes(wf.getnframes()),dtype="int16") / 32768.0
    return (data, fs)


print(read_wav('original.wav'))
