# -*- coding: utf-8 -*-
import numpy as np
import scipy.signal
import scipy.io.wavfile
import os


def read_wave(wavfile):
    ## -----*----- .wavファイルの読み込み -----*----- ##
    fs, wav = scipy.io.wavfile.read(wavfile)
    return (wav, fs)


def write_wave(wavfile, fs, wav):
    ## -----*----- .wavファイルに書き込み -----*----- ##
    if os.path.exists(wavfile):
        os.remove(wavfile)
    scipy.io.wavfile.write(wavfile, fs, wav)


def convert_fs(wav, fs, to_fs, to_int=True):
    ## -----*----- サンプリングレートを変換 -----*----- ##
    # wav : 変換対象の音源
    # fs  : 変換後のサンプリングレート

    converted = scipy.signal.resample(wav, int(wav.shape[0]*to_fs/fs))

    if to_int:
        converted = np.array(converted, dtype='int16')

    return (converted, to_fs)

