import cmath

def sumFreq(freq, data, frate):
  sum = 0+0j
  for t in range(len(data)):
    f=float(data[t])
    sum = sum + (f*cmath.e**((cmath.pi*2*t*(0+1j)*freq)/(frate)))
  return mag(sum)/len(data)

def checkFreq(freq, data, threshold, frate):
  return threshold < sumFreq(freq, data, frate)

def mag(c):
    a = c.real
    b = c.imag
    return (a**2 + b**2)**0.5
