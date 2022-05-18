def login():
	usernameInput = input("Enter Username : ")
	passwordInput = input("Enter Password : ")
	if usernameInput == "admin" and passwordInput == "1234":
		print("ยินดีต้อนรับ",usernameInput)
		showMenu()
	else:
		print("กรุณากรอกข้อมูลใหม่")
		login()

def showMenu():
	print("-------------- iShop -------------")
	print("1. Vat Calculator")
	print("2. Total Price Calculator")

	userSelect = int(input("กรุณาเลือกเมนู หรือกด 0 เพือออกจาก Program : "))
	return menuSelect(userSelect)

def menuSelect(userSelect):
	while userSelect !=0:
		if userSelect == 1:
			totalPrice = float(input("กรุณาใส่ราคา[THB] : "))
			return vatCalculate(totalPrice)
		elif userSelect == 2:
			return priceCalculate()
		else:
			print("----------กรุณาลองใหม่--------------")
			showMenu()
	else:
		print("---------ขอบคุณที่ใช้บริการ-------------")
		exit()

def vatCalculate(totalPrice):
	vat = 7/100
	print("Vat", "{:.0%}".format(vat), ": ", "{:,.2f}".format(totalPrice*vat))
	result = totalPrice*(1+vat)
	print("Total Vat Incl. : ", "{:,.2f}".format(result))
	return result, showMenu()

def priceCalculate():
	countItem = int(input("ใส่จำนวนสินค้าที่ต้องการ : "))
	totalPrice = 0
	for i in range(1, countItem+1):
		x = float(input("รายการสินค้าที่ :" + str(i) + " ราคา : "))
		totalPrice += x
	print("Total : ", "{:,.2f}".format(totalPrice))
	return vatCalculate(totalPrice), showMenu()

login()