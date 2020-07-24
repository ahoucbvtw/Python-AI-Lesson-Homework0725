import pymysql
import prettytable
import os

table = prettytable.PrettyTable(["MemberSerial","Name","BirthDay","Address","Telephone"], encodong = "utf8")
teltable = prettytable.PrettyTable(["TelephoneSerial","Telephone"], encodong = "utf8")

def ShowMemberList():
	#每次執行此函式都先清除table
	table.clear_rows()

	# cursor.execute("SELECT CONCAT(`id`,`name`),address FROM `member`")
	# data = cursor.fetchall()
	# for show in data:
	# 	print(show)
		# table.add_row([show[0],show[1],show[2],show[3]])
	# print(table)

	repeatSerial = ""
	cursor.execute("SELECT member.id, member.name, member.birthday, member.address ,tel.tel FROM `member` LEFT JOIN `tel` ON member.id = tel.member_id")
	data = cursor.fetchall()
	for show in data:
		if repeatSerial != show[0]:
			table.add_row([show[0],show[1],show[2],show[3],show[4]])
			repeatSerial = show[0]
		else:
			table.add_row(["","","","",show[4]])
	print(table)

def AddNewMember(Name, Birthday, Address):
	addmemberlist = [Name, Birthday, Address]
	sql = "INSERT INTO `member`(`name`,`birthday`,`address`) Values(%s,%s,%s)"
	cursor.execute(sql, addmemberlist)
	# 有改變動作完要加的(新增/刪除/更改值)
	database.commit()
	os.system("cls")
	print("新增完成！！\n")
	return "新增完成！！"

def RenewMember(ID, Name, Birthday, Address):
	ReMemberlist = [Name, Birthday, Address, ID]
	sql = "UPDATE `member` SET `name`= %s,`birthday`= %s,`address`= %s WHERE `id`= %s"
	cursor.execute(sql, ReMemberlist)
	database.commit()
	os.system("cls")
	print("更新完成！！\n")
	return "更新完成！！"

def DeleteMember(ID):
	DeleteList = [ID]
	sql = "DELETE FROM `member` WHERE `id`= %s"
	cursor.execute(sql, DeleteList)
	database.commit()
	#順便連tel資料表內所有一樣MemberID也一起刪除
	sql = "DELETE FROM `tel` WHERE `member_id`= %s"
	cursor.execute(sql, DeleteList)
	database.commit()
	os.system("cls")
	print("刪除完成！！\n")
	return "刪除完成！！"

def AddmemberTel(MemberID, Telephone):
	AddmemberTellist = [MemberID, Telephone]
	sql = "INSERT INTO `tel`(`member_id`, `tel`) Values(%s,%s)"
	cursor.execute(sql, AddmemberTellist)
	database.commit()
	os.system("cls")
	print("新增完成！！\n")
	return "新增完成！！"

def SearchMemberTel(MemberID):
	SearchMemberTellist = [MemberID]
	teltable.clear_rows()
	sql = "SELECT `id`, `tel` FROM `tel` WHERE `member_id` = %s"
	cursor.execute(sql, SearchMemberTellist)
	data = cursor.fetchall()
	for show in data:
		teltable.add_row([show[0],show[1]])
	print(teltable)

def DeleteMemberTel(TelID):
	DeleteMemberTellist = [TelID]
	sql = "DELETE FROM `tel` WHERE `id`= %s"
	cursor.execute(sql, DeleteMemberTellist)
	database.commit()
	os.system("cls")
	print("刪除完成！！\n")
	return "刪除完成！！"


# def CommendSelect(num_str, ID = None, Name = None, Birthday = None, Address = None, Telephone = None):
# 	command = {"0":os.system, "1":ShowMemberList, "2":AddNewMember, "3":RenewMember, "4":DeleteMember, "5":AddmemberTel}
# 	function = command.get(num_str)
# 	if function:
# 		if num_str == "0":
# 			function("exit")
# 		elif num_str == "1":
# 			function()
# 		elif num_str == "2":
# 			function(Name, Birthday, Address)
# 		elif num_str == "3":
# 			function(ID, Name, Birthday, Address)
# 		elif num_str == "4":
# 			function(ID)
# 		elif num_str == "5":
# 			function(ID, Telephone)

# 開啟資料庫連線
database = pymysql.connect(
	host = "localhost",
	user = "root",
	password = "",
	db = "python_ai",
	charset = "utf8"
)
# 使用 cursor() 方法建立一個遊標物件 cursor
cursor = database.cursor()

# #創建新Table
# cursor.execute("CREATE TABLE MemberSystem(Name char(50), Birthday date, Age int,Address text")

commandmsg = "(0)離開程式\n(1)顯示會員列表\n(2)新增會員資料\n(3)更新會員資料\n(4)刪除會員資料\n(5)新增會員電話號碼\n(6)刪除會員電話號碼\n請輸入指令："
connect = False

while True:
	#確認是否有連線到資料庫
	cursor.execute("SELECT VERSION()")
	# 使用 fetchone() 獲取單條資料
	data = cursor.fetchone()
	# print("Database version :", data[0])
	if data != []:
		connect = True
		inputcommand = input(commandmsg)
		try:
			int(inputcommand)
			if 0 <= int(inputcommand) <= 6:
				if inputcommand == "0":
					os.system("cls")
					break
				elif inputcommand == "1":
					os.system("cls")
					ShowMemberList()
				elif inputcommand == "2":
					os.system("cls")
					n_name = input("請輸入新進會員名字：")
					n_birthday = input("請輸入新進會員生日：")
					n_address = input("請輸入新進會員地址：")
					AddNewMember(Name = n_name, Birthday = n_birthday, Address = n_address)
				elif inputcommand == "3":
					os.system("cls")
					ShowMemberList()
					re_id = input("請輸入欲修改的會員編號：")
					re_name = input("請輸入欲修改的會員名字：")
					re_birthday = input("請輸入欲修改的會員生日：")
					re_address = input("請輸入欲修改的會員地址：")
					RenewMember(ID = re_id, Name = re_name, Birthday = re_birthday, Address = re_address)
				elif inputcommand == "4":
					os.system("cls")
					ShowMemberList()
					del_id = input("請輸入欲刪除的會員編號：")
					DeleteMember(ID = del_id)
				elif inputcommand == "5":
					os.system("cls")
					ShowMemberList()
					addtel_id = input("請輸入欲新增電話號碼的會員編號：")
					add_tel = input("請輸入欲新增的電話號碼：")
					AddmemberTel(MemberID = addtel_id, Telephone = add_tel)
				elif inputcommand == "6":
					os.system("cls")
					ShowMemberList()
					deltelmember_id = input("請輸入欲刪除電話號碼的會員編號：")
					SearchMemberTel(deltelmember_id)
					deletetel_id = input("請輸入欲刪除電話號碼的編號：")
					DeleteMemberTel(deletetel_id)

			else:
				os.system("cls")
				print("沒有這個指令！！\n")
				continue
		except:
			os.system("cls")
			print("請輸入正確指令！！\n")
			continue

	else:
		connect = False
		database = pymysql.connect(
			host = "localhost",
			user = "root",
			password = "",
			db = "python_ai",
			charset = "utf8"
		)
		cursor = database.cursor()

# 關閉資料庫連線
database.close()
os.system("exit")