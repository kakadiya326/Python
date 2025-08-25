previousMeter = int(input('Enter previous month readings : '))
currentMeter = int(input('Enter current month readings : '))
totalBill = currentMeter-previousMeter
if totalBill<=100:
    print('Your current month Electricity Bill is ',totalBill*2.5)
elif totalBill<=150:
    print('Your current month Electricity Bill is ',totalBill*5.7)
elif totalBill<=200:
    print('Your current month Electricity Bill is ',totalBill*7.2)  
elif totalBill<=150:
    print('Your current month Electricity Bill is ',totalBill*5.7)
else:
    print('Your current month Electricity Bill is ',totalBill*9.7)