
password = 'a123456'
j = 3       # 測試剩餘次數
while True:
	user = input("請輸入密碼: ")
	if user == password:
		print("登入成功!")
		break 
	else:
		j = j - 1
		print("密碼錯誤! 還有%d次機會" % j)
		if j ==0:
			break
		

