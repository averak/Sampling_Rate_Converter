Sampling Rate Converter
=======================

Convert the sampling rate of audio files in .wav format.


## Raquirement
- MacOS / Ubuntu 18.04
- Python 3.7
- numpy 1.18.1
- scipy 1.4.1
- wave 0.0.2


## Usage
```python
# read .wav file
wav, fs = read_wave('wav file path')
# ex) => wav : [...], fs : 8000

# up sampling (8000 -> 16000)
up_wav, up_fs = convert_fs(wav, fs, 16000)
# ex) => up_wav : [...], up_fs : 16000

# down sampling (8000 -> 4000)
down_wav, down_fs = convert_fs(wav, fs, 4000)
# ex) => down_wav : [...], down_fs : 4000
```
