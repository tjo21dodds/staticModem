import math

def getSinCoef(freq, period=44100):
    return ((2*math.pi)*freq)/period
