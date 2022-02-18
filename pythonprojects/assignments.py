#program to check if a given number is prime or not!
#num = int(input("Enter a number:"))
#if num != 1:
#    for i in range(2, num):
#        if (num % i == 0):
#            print(bool(0))
#            break
#    else:
#        print(bool(1))
#else:
#    print("Not a prime number!")             


#print first hundred prime numbers.
#prime_num = int(input("Enter a number:"))
#count= 2
#while prime_num != 0:
#     for i in range(2, count):
#         if (count % i == 0):
#             break
#     else:
#         print(count, end=" ")
#         prime_num -= 1
#     count += 1  

#sum of first 10 fibonacci sequence


#print first 300 prime num
#prime_counter = 0
#counter = 2 
#while prime_counter < 300:
#    for x in range (2, counter + 1):
#        if counter == 2 or counter == 3:
#            print(" ",counter, end=" ",sep="")
#            prime_counter += 1
#            break
#    
#        if x == counter:
#            print(" ",counter, end=" ",sep =" ") 
#            prime_counter += 1
#            if prime_counter % 15== 0:
#                print()
#        else:
#             if counter % x == 0:
#                break 
#    if counter % 100 == 0:
#        print()                
#    counter += 1  

#sum of digits of a positive integer number
#num = input("Enter a number:")
#sum = 0
#for x in str(num):
#    sum += int(x)
#    print(sum)

#sum of +ve digit integer also
num = input("Enter a number:") #input to enter a num
sum = 0 #by default
length = len(str(num))
digit_position = int("1"+ ("0"*(length-1)))
sum += num//digit_position
num = num % digit_position
#distance btw first 100 prime numbers 
#primecounter = 0
#counter=2
#prevprime=0
#while primecounter < 100:
#    for x in range(2, counter + 1):
#        if counter == 2 or counter == 3:
#            primecounter += 1
#            print(counter-prevprime, end=" ",sep=" ")
#            if primecounter == 1:
#                prevprime = counter
#            else:
#                print(counter - prevprime)
#                prevprime = counter
#                break
#        if x ==counter:
#            primecounter += 1
#            print(counter - prevprime)
#            prevprime = counter 
#        else:
#            if counter % x ==0: 
#                break
#    if counter % 100==0:
#        print()
#    counter += 1






