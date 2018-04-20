from time import strftime,localtime
import MySQLdb
import db
import serial
from multiprocessing import Process, Manager, Value
from ctypes import c_char_p,c_bool


def serial_write(buff_serial_write): # gui du lieu 
	port.write(buff_serial_write.value.encode())
	buff_serial_write.value=""

def serial_loop(buff_serial_read,buff_serial_write,buff_serial_coppy,serial_en):
	print(serial_en.value)
	while True:
		serial_process1(buff_serial_read,buff_serial_write,buff_serial_coppy,serial_en)

def serial_process1(buff_serial_read,buff_serial_write,buff_serial_coppy,serial_en): # theard nhan du lieu ghi vao buff nhan duoc ki tu ket thuc thi chay theard xu ly du lieu 
	rev= port.read(1)
	if serial_en.value ==True:
		if rev =="^":
			buff_serial_coppy.value=buff_serial_read.value
			print (buff_serial_coppy.value)
			process_hand = Process(target=serial_hand, args=(buff_serial_write,buff_serial_coppy,))
			process_hand.start()
			process_hand.join()
			serial_en.value=False
			buff_serial_read.value =""
		else :
			if rev == "@":
				buff_serial_read.value =""
			else :
				buff_serial_read.value=buff_serial_read.value + rev
				pass
	else: 
		if rev =="@":
			serial_en.value =True
				
def serial_hand(buff_serial_write,buff_serial_coppy) :
	# try: #  neu co loi thi chay except
	string= buff_serial_coppy.value
	data = string.split( )
	if data[0]=="P":
		ID_zigbee = data[1]
		ADDR_zigbee= data[2]
		
		print(ID_zigbee + ADDR_zigbee)
	
		
	# except:
		# print("Loi chuoi json UART: " + str(buff_serial_coppy.value) ) # print ra chuoi loi
		
if __name__ =="__main__" :	
	port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0) # khoi tao UART
	print(port)
	manager = Manager() # khoi rao bien 
	buff_serial_read = manager.Value(c_char_p,"")  # buff doc du lieu 
	buff_serial_write = manager.Value(c_char_p,"") # buff ghi du lieu
	buff_serial_coppy = manager.Value(c_char_p,"sfasf") # buff xu li du lieu
	serial_en = manager.Value(c_bool,False)				# bien cho phep nhan du lieu (khi nhan dc ki tu dau tien $)
	process_serial = Process(target=serial_loop, args=(buff_serial_read,buff_serial_write,buff_serial_coppy,serial_en,))
	process_serial.start()
	process_serial.join() 
	
	
	
	
	
	
