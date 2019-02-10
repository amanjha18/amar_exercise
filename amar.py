# # 1.....................................................................................................
# # divisible by 3 and 5.
# # user=int(input("enter the number"))
# # for i in range(1,user):
# # 	if i%3==0 or i%5==0:
# # 		print i


# # 2.....................................................................................................
# #Leap year.
# # user=int(input("enter the number, check leap year:  " ))
# # if user%100==0 and user%400==0:
# # 	print "leap year hai"
# # elif user%4==0 and user%100!=0:
# # 	print "leap year hai" 
# # else:
# # 	print "leap year nahi hai"

# # 3.....................................................................................................

# # prevous 3 even and previous 3 odd.
# a=int(input("enter the number "))
# b=1
# c=2
# if a%2==0:
#     for i in range(0,3):
#         print a-c,
#         print a+b
#         c=c+2
#         b=b+2
# else:
#     for i in range(0,3):
#         print a+c,
#         print a-b
#         b=b+2
#         c=c+2

# # 4..........................................................................................

# # user=int(input("enter the year"))
# # year = user
# # count = 0
# # while True:
# #     if user%100 == 0 and user%400 == 0:
# #         user+=4
# #         print user
# #         count +=1
# #     elif user%4 == 0 and user%100!=0:
# #         user+=4
# #         print user
# #         count+=1
# #     elif user%4!=0:
# #         user-=1
# #     elif user%4==0:
# #         user+=4
# #         print user
# #         count+=1
# #     if count == 3:
# #         break
# # count = 0
# # user = year
# # while True:
# #     if user%100==0 and user%400==0:
# #         user-=4
# #         print user
# #         count+=1
# #     elif user%4==0 and user%100!=0:
# #         user-=4
# #         print user
# #         count+=1
# #     elif user%4!=0:
# #         user+=1
# #     elif user%4==0:
# #         user-=4
# #         print user
# #         count+=1
# #     if count ==3:
# #         break



# #4.................................................................................................

#code for armstrong number.
# a=raw_input("enter the number")
# sum=0
# for i in range(0,len(a)):
#    b=int(a[i])**len(a)
#    sum=b+sum
# if str(sum)==a:
# 	print "armstrong number hai"
# else:
#     print "armstrong number nahi hai"

# #...............................................................................................

#code for armstrong number.

# a=input("enter the number")
# for j in range (1,a):
# 	j=str(j)
# 	sum=0
# 	for i in (j):
# 		b=int(i)**len(j)
#     	sum+=b
# 	if str(sum)==j:
# 		print j




# #5............................................................................................
#prime factor
# a=input("enter")
# b=[]
# for i in range(2,a):
#     if a%i==0:
#         b.append(i)
# for j in b:
#     for k in range(2,j):
#         if j%2==0:
#             break
#     else:
#         print j



#prime factor
# a=20
# for i in range(2,a+1):
# 	if a%i==0:
# 		for j in range(2,i):
# 			if i%j==0:
# 				break
# 		else:
# 			print i


#6   ##################################################
# code to find the power of a number

# a = int(input("enter a number: "))
# b = int(input("enter the power: "))
# mul = 1
# for i in range(b):
# 	mul = mul*a
# mul = str(mul)
# sum = 0
# for j in mul:
# 	sum = int(j) + sum
# print (sum)

#7   #####################################################
#Anagram.

# a=raw_input("enter input check anagram no.: ")
# b=raw_input("enter input check anagram no.: ")
# a=list(a)
# b=list(b)
# a.sort()
# b.sort()
# if a==b:
# 	print "output: "+" anagram hai"
# else:
# 	print "output: "+"anagram nahi hai"


#############################################################

# a=raw_input("enter your input ")
# if len(a)>=2:
#     b=a[:2]
#     c=a[-2:]
#     print str(b+c)
# else:
    # print"EMPTY"

#################################################################

# a=raw_input("enter input: " )
# # # a=list(a)
# # # b=[]
# # # for i in a:
# # #     b.append(i)
# # # b.pop()
# # # print b

# if "ing" not in a:
# 	b=a+"ing"
# 	print b
# else:
# 	if "ing" in a:
# 		c=a+"ly"
# 		print c   

#####################################################################

#fibonacci even.
# user=int(input("enter"))
# a=0
# b=1
# c=0
# for i in range(user):
#     if a%2==0:
#         print a
#     c=a+b
#     a=b
#     b=c

#######################################################################

# a=int(input("enter the number"))
# sum=0
# b=1
# for i in range(a+1):
#     b=i**2
#     sum=sum+b
# d=0
# for j in range(a+1):
#     d=j+d
# e=d**2
# print e-sum

########################################################################

# a=int(input("enter input for factorial "))
# b=1
# for i in range(1,a+1):
#     b=i*b
# print b

######################################################################


# a=raw_input("enter your input: ")
# sum=0
# for i in a:
#     i=int(i)
#     sum=i+sum
# print sum


##################################################################
# code for factorial addition string intigers.
# a=raw_input("enter the input: ")
# b=1
# sum=0
# for i in a:
#     i=int(i)
#     for j in range (1,i+1):
#         b=j*b
#     sum=sum+b
#     b=1
# print sum

###################################################################

# a=" 34122"
# print a[::-1]

######################################################################

# number=int(input("enter the number "))
# power=int(input("enter the power "))
# a=number**power
# a=str(a)
# sum=0
# for i in a:
# 	sum=sum+int(i)
# print sum

#######################################################

# dic1={"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
# user = input("enter a input: ")
# a = user.split()
# sum = 0
# for i in a:
#     a = dic1[i]
#     sum = sum + a
# print (sum)

#################################################################################

# a = input("enter an input: ")
# if a[-1] == 'e':
#     var = a[:-1] + 'ing'
#     print (var)
# elif a[-1] == 'y':
#     b = ''
#     for i in range(len(a)-1, len(a)-3, -1):
#         b = b + a[i]
#     else:
#         if b == 'yl':
#             print (a)
# elif a[-1] == 'g':
#     var = ''
    
#     for i in range(len(a)-1, len(a)-4, -1):
#         var = var + a[i]
#     else:
#         if var == 'gni':
#             a = a + 'ly'
#             print (a)
# else:
#     print (a+'ing')




   