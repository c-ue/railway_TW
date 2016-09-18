import sys
import wave

for arg in sys.argv[1:]:
    with open(arg, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    with wave.open(arg+'1.wav', 'wb') as wavfile:
        wavfile.setparams((1, 1, 8000, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)