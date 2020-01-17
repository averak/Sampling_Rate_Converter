import numpy as np
import scipy.signal
import struct
import wave


def read_wav(file):
    ## -----*----- Wavファイルの読み込み -----*----- ##
    wf = wave.open(file)
    fs = wf.getframerate()

    wav = np.frombuffer(wf.readframes(wf.getnframes()), dtype="int16")
    return (wav, fs)


def change_sampling(wav, fs,  change_fs):
    ## -----*----- Wavファイルの読み込み -----*----- ##
    # FIRフィルタの用意をする
    nyqF = fs / 2.0                      # 変換後のナイキスト周波数
    cF   = (fs / 2.0-500.0)/nyqF         # カットオフ周波数を設定
    taps = 511                           # フィルタ係数(odd)

    # 変換後の音声を格納
    converted = []

    if fs < change_fs:
        # Up Sampling
        SampleNum = int(change_fs / fs - 1)
        for d in wav:
            converted.append(d)
            for i in range(SampleNum):
                converted.append(converted[-1])

    elif fs > change_fs:
        # Down Sampling
        SampleNum = int(fs / change_fs - 1)
        for i in range(0, len(wav), SampleNum+1):
            converted.append(wav[i])

    else:
        # 変換しない
        converted = wav

    return (np.array(converted), change_fs)


def write_wav(file, wav, fs):
    # データを-32768から32767の整数値に変換
    wav = [int(x) for x in wav]
    wf = wave.Wave_write(file)
    b_wave = struct.pack("h" * len(wav), *wav)
    wf.setparams((
        1,                          # channel
        2,                          # byte width
        fs,                         # sampling rate
        len(wav),                   # number of frames
        "NONE", "not compressed"    # no compression
        )
    )
    wf.writeframes(b_wave)
    wf.close()

