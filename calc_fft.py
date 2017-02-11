from scipy.fftpack import fft
from pylab import *
from pandas import read_csv

def calc(d,T):
    N = len(d)
    yf = fft(d)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    return xf, 2.0/N * np.abs(yf[0:N//2])


def test():
    a = sin(linspace(0,100,1000))
    b = sin(0.5*linspace(0,100,1000))
    d = a+b
    x,y = calc(d,0.1)
    plot(x,y)
    show()

def rolling_score(fname,lowF,hiF,N,T):
    a=read_csv(open(fname))
    raw = a['eegRawValue']
    score = []
    for i in range(N,len(raw)):
        x,y = calc(raw[i-N:i],T)
        idx = [i for i in range(len(x)) if x[i]>=lowF and x[i]<=hiF]
        score.append(sum(y[idx])/len(idx))
    return score



def mindwave():
    a=read_csv(open('eegIDRecord-3.csv'))
    raw = a['eegRawValue'][8000:]
    x,y = calc(raw,0.01)
    lowF = 8
    hiF = 12
    idx = [i for i in range(len(x)) if x[i]>=lowF and x[i]<=hiF]
    print sum(y[idx])/len(idx)
    plot(x,y)
    show()

if __name__=="__main__":
    # mindwave()
    delta = rolling_score('eegIDRecord-3.csv',4,8,1000,0.01)
    semilogy(delta);
    alpha = rolling_score('eegIDRecord-3.csv',8,12,1000,0.01)
    semilogy(alpha);
    beta = rolling_score('eegIDRecord-3.csv',12,20,1000,0.01)
    semilogy(beta);

    show()

