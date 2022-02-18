 #def raise_to_pow(base_num, pow_num):
 #   result = 1
  #  for index in range(pow_num):
   #     result = result * base_num
    #return result 
#print(raise_to_pow(3,3))        

  #code to print prime numbers
#start = int (input("Enter the start range:"))   
#end = int (input("Enter the end range:"))   
#print ("prime numbers in the range", start, "to", end)
#for i in range(start, end):
#    flag = 0
#    for j in range(2, i):
#        if (i % j == 0):
#            flag = 1
#           break
#    if (flag == 0):
#        print(i, end ="\t")   

#prime numbers using boolean values
num = int(input("Enter a number:"))
if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print(False)
            break
    else:
        print(True)
else:
    print(num , "is not a prime number")