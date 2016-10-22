source1=r'65179-pcm.wav'
source2=r'701601-pcm.wav'


import os
import subprocess
os.chdir(r'C:\Users\apple\Desktop\git\railway_TW\ffmpeg\bin')
subprocess.call(['ffmpeg', '-i', '../../65179.wav','-c:a','pcm_s16le', '1.wav'])
exit()

import speech_recognition as sr
import  time,random 
def voice2text(sfile):
    r = sr.Recognizer()
    with sr.WavFile(sfile) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio_data=audio, language='zh_TW')
    except LookupError:
        return False 
        
