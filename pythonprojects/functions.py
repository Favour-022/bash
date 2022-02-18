#def changelist (mylist):
#    mylist.append(5)
#    print ("Values inside function", mylist)
#    return mylist
#mylist= [3,4,5]
#changelist (mylist)
#print ("Values outside function",mylist)

#def sum_maker (number_list):
#    "Finds and returns sum using list"
#    list_sum = 0
#    for num in number_list:
#        list_sum += num
#    return list_sum

#print ("sum of [4,6,7] is ", sum_maker([4,5,6]))
#print (sum_maker.__doc__)

#def sumall(a,b,c,d=10,*e):
#    result = a+b+c+d
#    for i in e:
#        result += i 
#    return result

#def print_num(num):
#    num = 0
#   while num <= 10:
#        print(num)
#        num += 1    

#print_num(10)

#def factorial(ten_factorial):
#    result = 1
#    for x in range(1,11):
#        result *= x
#    return result

#print(factorial(10))   
        

#temp conversion
#def conversion(temp):
#    
#    result = 9/5 * temp + 32
#    return result
#print(conversion(27))   

#sum of array of numbers
# def sum_array(mylist):
#    result = 0
#    for x in mylist :
#        result += x
#    return result

# num_list = [1,2,3,4,5]  
# print (sum_array(num_list))


# def addNumbers(nums):
#     result = 0
#     for i in nums:
#         result += i 
#     return result

# nums = [1,2]
# print (addNumbers(nums)


# def postiveNumber(num):
#     "function that returns and prints postive integers in an array"
#     nums = []
#     for i in num:
#         if i >= 0:
#             nums.append(i)

#     return nums 
       


# nums = [0,-2,5,-8,6,4,2,-1,1,6]
# print(postiveNumber(nums))

#function to check if a number is prime
# def primeNum(isPrime):
#     if num != 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 return (bool(0))
#                 break
#             else:
#                 return(bool(1))

# num= 19
# print(primeNum(num))

#max number in an array of numbers
# def maxNum(num):
#     for i in num:
#         return max(num)

# mylist = [7,5,6,4,3,2,9,0,8]
# print(maxNum(mylist))       


# def fibbonacciseq(s,n):
#     "this function finds the nth fibonacci number"
#     a=b=c=s
#     for i in range of (1,n+1):
#         if i >2:
#             c =a+b
#             a,b=b,curr
#     return c
# print(fibbonacciseq(1,4))

#recursive fibonnacci sequence
def recfibonnacciseq(s,n):
    if n < 3:
        return s 
    else:
        return recfibonnacciseq(s,n-2)+ recfibonnacciseq(s,n-1)

print(recfibonnacciseq(1,5))      




# def longestSubstring(string):
#     "this function returns the longest substring without repeating character"
#     prev = ""
#     curr = ""
#     for x in range(0,len(string)):
#         if string[x] in curr:
#             prev = prev if len(prev) > len(curr) else curr
#             curr = "" + string[x] #try removing + string[x]
#         else:
#                 curr += string[x]

#     return prev

# string = "wednesdays"
# print(longestSubstring(string))

# def iseven(x):
#     "tests if a number is even using recursion"
#     if x < 0:
#         return False
#     if x == 0:
#         return True
#     if x == 1:
#         return False

#     return iseven(x-2)
# print(iseven(20))