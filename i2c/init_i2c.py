import smbus
#sudo apt-get install python-smbus
import time

bus=smbus.SMBus(2)

#The i2c slave address for HMC5883
address=0x1e

def read_register(addr):
#read data from address:addr
	global bus
	global address
	data=bus.read_byte_data(address,addr)
	print data

for i in range(0,30):
	print i,':',
	read_register(i)
