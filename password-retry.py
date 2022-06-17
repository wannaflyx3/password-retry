#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確 就印出"登入成功"
#如果不正確 進印出"密碼錯誤，還有__次機會

'''password = 'a123456'
i = 3 #剩餘機會
while True:
	password1 = input('請輸入密碼:')
	
	if password == password1:
		print('登入成功')
		break  #跳出迴圈
	else:
		i -= 1
		print('密碼錯誤，還有',i,'次機會')
		if i == 0:
			break'''

password = 'a123456'
i = 3 #剩餘機會
while i > 0:
	password1 = input('請輸入密碼:')
	
	if password == password1:
		print('登入成功')
		break  #跳出迴圈
	else:
		i -= 1
		print('密碼錯誤，還有',i,'次機會')




