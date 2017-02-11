import serial
from pylab import *
import time
import cPickle

ser = serial.Serial(
    port='/dev/tty.usbserial-AL027QGH',\
    baudrate=57600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
ser.flushInput()
ser.flushOutput()

#this will store the line
line = []
cnt = 0
data = []
start = time.time()
while True:
    cnt += 1
    # print '------------>',cnt
    line = []
    for c in ser.readline():
        line.append(bin(ord(c)))
        print line
        if ord(c)==165:
            parsed_line = line[4:-1]
            # print parsed_line
            a = parsed_line[::2]
            b = parsed_line[1::2]
            if len(a)==6 and len(b)==6:
                data.append([int(a[i][2:]+b[i][2:],2) for i in range(6)])
                print data[-1]
            line = []
    # print len(data)
    if not len(data) % 300:
        cPickle.dump(data,open('data.pick','w'))
    # ser.flushInput()
    # ser.flushOutput()
data = array(data)
print data
print time.time() - start
plot(data[:,0])
show()
plot(data[:,1])
show()
plot(data[:,2])
show()
plot(data[:,3])
show()
plot(data[:,4])
show()
plot(data[:,5])
show()

ser.close()
time.sleep(1)
