import os
import glob
import numpy as np
import librosa as lr
import soundfile as sf

# 대상 폴더 경로
source_folder = "audio"
destination_folder = "audio"

# 대상 폴더 내 모든 PCM 파일
pcm_files = glob.glob(os.path.join(source_folder, "*.pcm"))

for target in pcm_files:
    destinationPath = os.path.join(destination_folder, os.path.basename(target).replace(".pcm", ".wav"))

    buf = None
    with open(target, 'rb') as tf:
        buf = tf.read()
        buf = buf + b'0' if len(buf) % 2 else buf

    pcm_data = np.frombuffer(buf, dtype='int16')
    wav_data = lr.util.buf_to_float(x=pcm_data, n_bytes=2)

    # WAV 저장
    sf.write(destinationPath, wav_data, 16000, format='WAV', endian='LITTLE', subtype='PCM_16')

    print(f"Converted {target} to {destinationPath}")
