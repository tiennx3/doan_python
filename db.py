from time import strftime,localtime
import MySQLdb
DEBUG_APP=True
# Mysql connection
def connect():
    return MySQLdb.connect(host="localhost" , user="root", passwd="toor" , db="nurs_home")
def getdatacur(id_zigbee):
	db = connect()
	cur=db.cursor()
	cur.execute("""SELECT * FROM nurs_home.profile where ID_ZIGBEE=%s;""",id_zigbee)
	row_count = cur.rowcount
	if DEBUG_APP==True:
		print ("getdata.row_count:"+str(row_count))
	return cur
	db.close()
	
def checknulldata(curcheck) :
	row_count = curcheck.rowcount
	if DEBUG_APP==True:
		print (row_count)
	if row_count==1:
		if DEBUG_APP==True:
			print ("checknull:check ok)")
		return 1;
	else :
		if DEBUG_APP==True:
			print ("checknull:check not")
		return 0;

def inserttobanghi(id_zigbee,addr_zigbee,name,ngaysinh,sdt,thongbao,trangthai):
	thoigian= strftime("%d-%m-%Y %H:%M:%S", localtime())
	db = connect()
	cur=db.cursor()
	cur.execute("""INSERT INTO ban_ghi (ID_ZIGBEE, ADDR_ZIGBEE, TEN, NGAYSINH, SODT, THONGBAO, TRANGTHAI, THOIGIAN) VALUES (%s, %s, %s,%s, %s, %s, %s, %s)""",(id_zigbee,addr_zigbee,name,ngaysinh,sdt,thongbao,trangthai,thoigian))
	db.commit()
	db.close()
	action =True
	return action	
		
	
	
	
# Write card readings to database
def write(tagId,action):
    db = connect()
    c = db.cursor()
    currentTime=strftime("%d-%m-%Y %H:%M:%S", localtime())
    c.execute("""INSERT INTO readings (tagId, time, action) VALUES (%s, %s, %s)""",(tagId,currentTime,action))
    db.commit()
    db.close()
    action ="Submitted. Have a nice day!"
    return action

# Write new card registration to database 
def writeUser(userId,tagId,permission):
    db = connect()
    c = db.cursor()
    added=strftime("%d-%m-%Y %H:%M:%S", localtime())
    c.execute("""INSERT INTO cards (userId, tagId, added, permission) VALUES (%s, %s, %s, %s)""",(userId,tagId,added,permission))
    db.commit()
    db.close()
    action ="New card user added!"
    return action