##2 Calculate flight cost based on destination city. Print the cost.

destinationcity = input('Enter your destination city: ')
print()
##3
daysaway = input('Enter the number of days for your hotel stay: ')
print()

##4
if destinationcity == "Tokyo":
  print("Tokyo is SGD 818")
elif destinationcity == "Kuala Lumpur":
  print("Kuala Lumpur is SGD 245")
elif destinationcity == "Bangkok":
  print("Bangkok is SGD 359")
elif destinationcity == "Taipei" :
  print("Taipei is SGD 645")
else: print("City not found")
