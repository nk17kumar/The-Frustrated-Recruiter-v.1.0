from user import *
from hidden import *
from writer import *
from compiler import *
import subprocess
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('BlindCode-6a1c6b8f83f7.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("BlindCode").sheet1
reg_no = raw_input("Enter Regestration No : ")
name=raw_input("Enter Name : ")
roll_no=raw_input("Enter Roll number : ")
lang=raw_input("Enter Prefered Language : ")
user=User(reg_no,name,roll_no,lang)
time_left = 300
path = os.path.abspath("../resources")
path = path + "/code."
ext = ""
if lang == "c" :
	ext = "c"
if lang == "c++" :
	ext = "cpp"
if lang == "java" :
	ext = "java"
if lang == "python" :
	ext = "py"
path = path + ext
sr = subprocess.call(["clear"])
while time_left > 0 :
	print "Enter $ to exit, start your code you have %d seconds to complete : " %(time_left)
	code = hidden.blind_string(user)
	writer.write_code(lang,code)
	compiled=Operation.run_compiler(lang)
	time_left = 300 - user.get_time()
	print ""
	if compiled == "no_err" :
		AC = Operation.check_ac()
		AC += 10
		if AC != 10.0 :
			if time_left > 0 :
				AC += 0.1*float(time_left)
			print "Compiled and accepted"
			user.set_status("Compiled and accepted")
		else :
			print "compiled - Wrong Answer"
			user.set_status("compiled - Wrong Answer")
		print "score : %.2f " %(AC)
		user.set_score(AC)
	elif compiled == "cm_err" :
		print "Compilation Error"
		Operation.show_compilation_err(compiled)
		user.set_status("compilation error")
		print "Try Again"
	else :
		print "Runtime Error"
		Operation.show_compilation_err(compiled)
		user.set_status("Runtime Error")
		AC = Operation.check_ac()
		AC += 10
		if time_left > 0 :
			AC += 0.1*float(time_left)
		print "score : %.2f " %(AC)
		user.set_score(AC)
	sr = subprocess.call(["gedit",path])
	print "Time left : %d seconds" %(time_left)
	loop = raw_input("Want to continue Y/N : ")
	if loop == 'N' or loop == 'n' :
		break
	sr = subprocess.call(["clear"])
cells = "A" + str(int(reg_no)+1) + ":G" + str(int(reg_no)+1)
cell_list = wks.range(cells)
# # Update values
cell_list[0].value = reg_no
cell_list[1].value = name
cell_list[2].value = roll_no
cell_list[3].value = lang
cell_list[4].value = user.get_status()
cell_list[5].value = user.get_time()
cell_list[6].value = user.get_score()
# Send update in batch mode
wks.update_cells(cell_list)
print user
