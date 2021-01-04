import wave
import numpy as np
import matplotlib.pyplot as plt
import math
import fourier
import wavUtils as wu
import byteInterpreter as bi

baseline = 100
seperation = 5
density = 8
dur = 0.1
frate = 44100

def getData(fileName):
    data = []
    file =  wave.open(fileName)
    n = file.getnframes()
    audio = file.readframes(n)
    file.close()
    return np.frombuffer(audio, dtype=np.int16)

def writeData(fileName, byteTable):
    frate = 44100
    width = 2
    with wave.open(fileName, 'wb') as file:
        file.setnchannels(1)
        file.setsampwidth(width)
        file.setframerate(frate)
        file.setnframes(len(byteTable)*(frate//10))
        for t in range(len(byteTable)):
            for a in range(frate//10):
                value = int(calFrameVal(byteTable[t], (t*(frate//10)+a)))
                for i in range(width):
                    b = value % 256
                    value = (value - b)//256
                    file.writeframesraw(bytes([b]))

def calFrameVal(byte, pos):
    value = 0
    for i in range(len(byte)):
        if byte[i] == '1':
            value = value + (1000*math.sin(wu.getSinCoef(baseline*seperation*(i+1))*pos))
    return int(value)

def readData(fileName, split):
    data = getData(fileName)
    string = ""
    for segment in range(len(data)//int(frate*dur)):
        string = string + getBinFor(data[segment*int(frate*dur): (segment+1)*int(frate*dur)],split)
    print(string)
    return bi.textFromBits(string)


def getBinFor(segment, split):
    string = ""
    for i in range(split):
        freq = baseline * seperation * (i + 1)
        if fourier.checkFreq(freq, segment, 10.0, frate):
            string = string + '1'
        else:
            string = string + '0'
    return string

inStr =""
with open("input.txt") as f:
    inStr = f.read()

# writeData("./testData/output/out1.wav", bi.textToByteTable(inStr, split = density))
# result = getData("./testData/output/out1.wav")
print(readData("./testData/output/out1.wav",density))
