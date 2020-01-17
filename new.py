# -*- coding: utf-8 -*-
import numpy as np
import scipy.signal
from scipy.io.wavfile import read


def read_wave(wavfile):
    ## -----*----- .wavファイルの読み込み -----*----- ##
    fs, wav = read(wavfile)
    return (wav, fs)



wav, fs = read_wave('./original.wav')
print(wav, fs)
