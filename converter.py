import numpy as np
import scipy.signal
import wave


def read_wav(file):
    ## -----*----- Wavファイルの読み込み -----*----- ##
    wf = wave.open(file)
    fs = wf.getframerate()

    wav = np.frombuffer(wf.readframes(wf.getnframes()), dtype="int16")
    return (wav, fs)


def change_sampling(wav, fs,  change_fs):
        # FIRフィルタの用意をする
        nyqF = fs / 2.0                      # 変換後のナイキスト周波数
        cF   = (fs / 2.0-500.0)/nyqF         # カットオフ周波数を設定
        taps = 511                           # フィルタ係数(odd)
        b    = scipy.signal.firwin(taps, cF) # LPFを用意

        # 変換後の音声を格納
        converted = []

        if fs < change_fs:
            # Up Sampling
            SampleNum = int(change_fs / fs - 1)
            for d in wav:
                converted.append(d)
                for i in range(SampleNum):
                    converted.append(converted[-1])
            converted = scipy.signal.lfilter(b, 1, converted)

        elif fs > change_fs:
            # Down Sampling
            SampleNum = int(fs / change_fs - 1)
            wav = scipy.signal.lfilter(b, 1, wav)
            for i in range(0, len(wav), SampleNum+1):
                converted.append(wav[i])

        else:
            # 変換しない
            converted = wav

        return (np.array(converted), change_fs)



wav, fs = read_wav('original.wav')
rewav, _ = change_sampling(wav, fs, 16000)
print(len(wav), len(rewav), rewav)
