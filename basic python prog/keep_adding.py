#keep adding the string number till enter is pressed
sum = 0
while(True):
   userInput = input("Enter your price and press q to quit\n")
   if(userInput != "q"):
      sum=sum + int(userInput)
      print(f"sum till is {sum}")
   else:
          break
print(f"Total Amount is {sum}")