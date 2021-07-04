with open('C://Users//GIGABYTE//Desktop//python coding//currency converter//currency.txt') as f:
 lines = f.readlines()

 currencydict = {}
 for line in lines:  
    data = line.split('\t')
    currencydict[data[0]]= data[1]
   

 amount = int(input("Enter the amount"))
 print("Enter the name of currency you want to convert available options \n")
 for items in currencydict.keys():
   print(items)



 currency = input("Enter the available options")
 result = amount*float(currencydict[currency])
 print(f"{amount} in INR is {result} in  {currency}")