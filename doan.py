from time import strftime,localtime
import MySQLdb
import db
# db = MySQLdb.connect(host="localhost" , user="root", passwd="toor" , db="nurs_home")
# cur = db.cursor()
# cur.execute("SELECT STT,ID_ZIGBEE FROM ban_ghi")
# data="00000000001"
# cur.execute("INSERT INTO nurs_home.add_device (ID_ZIGBEE) VALUES (%s);",data)
tagId = "0000000005"
currentTime = "hello"
action = "sdss"
db1 =db.connect()
c=db1.cursor()
data1 = db.getdatacur(tagId)
db.checknulldata(data1)
a=db.inserttobanghi("0000000003","0x0098","Nguyen Van A","22-1-1856","0184048090923","THONG BAO","NGA NGUA")
print a
# cur.execute("""INSERT INTO add_device (ID_ZIGBEE, ADDR_ZIGBEE, TIME) VALUES (%s, %s, %s)""",(tagId,currentTime,action))
# db.commit()
# for row in cur.fetchall() 
      # data from rows
        # firstname = str(row[0])
        # lastname = str(row[1])

      # print it
        # print "The first name is " + firstname
        # print "The last name is " + lastname
currentTime=strftime("%d-%m-%Y %H:%M:%S", localtime())
print (currentTime)