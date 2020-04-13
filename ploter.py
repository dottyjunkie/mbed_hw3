import matplotlib.pyplot as plt
import numpy as np
import serial
import time


x = []
y = []
z = []
tilt = []

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)
for i in range(0, 100):
	line = s.readline()
	
	sline = line.decode().split(",")
	print(i)
	print("is")
	print(sline)
	if(len(sline)==4):
		try:
			x.append(float(sline[0]))
			y.append(float(sline[1]))
			z.append(float(sline[2]))
			tilt.append(int(sline[3][0]))
		except:
			print(i)

t = np.arange(0,float(len(x))/10, 0.1)
print("-----------------")
print(len(x))
print(len(t))
fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x, 'r', label = "X")
ax[0].plot(t, y, 'g', label = "Y")
ax[0].plot(t, z, 'b', label = "Z")
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend()

ax[1].stem(t, tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')

plt.show()
s.close()