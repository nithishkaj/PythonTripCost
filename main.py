##1 Print a list of cities

print('Tokyo \nKuala Lumpur \nBangkok \nTaipei')
print()

##2 Ask the user for the destination city

destinationcity = input('\nEnter your destination city: ')

##3 Ask for the numbers of days user will be away

daysaway = input('\nEnter the number of days for your hotel stay: ')
print()

##4 Calculate flight cost based on destination city. Print the cost.

def flightamount():
  if destinationcity == "Tokyo":
    return float(818)
  elif destinationcity == "Kuala Lumpur":
    flightamount = 245
  elif destinationcity == "Bangkok":
    flightamount = 359
  elif destinationcity == "Taipei" :
    flightamount = 645
  else: 
    print("City not found")

print('Total flight cost is',flightamount())

##5 Calculate hotel cost based on the destination city and days. Print the cost.

sumamt = 0

if destinationcity == "Tokyo":
  sumamt = int(192) * int(daysaway)
  print("\nYour total cost for hotel stay in Tokyo will be SGD",sumamt)
elif destinationcity == "Kuala Lumpur":
  sumamt = int(72) * int(daysaway)
  print("\nYour total cost for hotel stay in Kuala Lumpur will be SGD",sumamt)
elif destinationcity == "Bangkok":
  sumamt = int(88) * int(daysaway)
  print("\nYour total cost for hotel stay in Bangkok will be SGD",sumamt)
elif destinationcity == "Taipei" :
  sumamt = int(90) * int(daysaway)
  print("\nYour total cost for hotel stay in Taipei will be SGD",sumamt)


##Calculate the total cost of the trip and print it.

sum = flightamount() + hotelamount()

print("\nYour total trip costs", "(",flightamount,"+",sumamt,")","=","SGD", sum)

