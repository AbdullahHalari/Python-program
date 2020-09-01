# ###task 1 : make a calculator

# num1 = int(input ("enter first number"))
# num2 = int(input ("enter second number"))
# print("the sum is",num1+num2)
# print("the sum is",num1-num2)
# print("the sum is",num1*num2)
# print("the sum is",num1/num2)

# #-----------------------------------------------------------------------------

# #task 2: precent calculator

# cp = int(input ("enter marks of cp"))
# itc = int(input ("enter marks of itc"))
# calculus =int(input ("enter marks of calculus"))
# english = int(input ("enter marks of english"))
# islamiat = int(input ("enter marks of islamiat"))
# result = (cp + itc + calculus + english + islamiat )*100
# percent = result /250
# print("the percentage is:",percent)

# #--------------------------------------------------------------------------------

# #task 3 finding roots
# a = 25**(1/3)
# b = 200**(1/8)
# c = 64**(1/2)
# print("cube root of 25 is 25**(1/3) :",a)
# print("eight root of 200 is 200**(1/8) :",b)
# print("square root of 64 is 64**(1/2) :",c)

# #---------------------------------------------------------------------------------------



# #task 4

# num1 = input ("enter  item")
# num2 = input ("enter item")
# num3 = input ("enter  item")
# num4 = input ("enter  item")
# num5 = input ("enter item")

# firstlist = [num1,num2,num3,num4,num5]
# print(firstlist)

# secondlist = [0]
# num1 = int(input ("enter first number"))
# secondlist.append(num1)
# num2 = int(input ("enter first number"))
# secondlist.append(num2)
# num3 = int(input ("enter first number"))
# secondlist.append(num3)
# num4 = int(input ("enter first number"))
# secondlist.append(num4)
# num5 = int(input ("enter first number"))
# secondlist.append(num5)

# sumlist = secondlist[1]+secondlist[2]+secondlist[3]+secondlist[4]+secondlist[5]
# print("the sum is: ",sumlist)
# avg = sumlist/5
# print("the avg is:",avg)





 

# choice = str(input("Enter your choice: triangle,rectangle,circle "))
# if(choice=='triangle'):
#  def triangle (h,b):
#     area = h*b/2
#     return(area)
#  triangle(h,b)
#  value_1 = int(input("enter height: "))
#  value_2 = int(input("enter base: "))
#  print("The area of triangle is: ",triangle(value_1,value_2))
# elif(choice=='rectangle'):
#  def rectangle (w,l):
#     area_1 = w*l
#     return(area_1)
#  rectangle(w,l)
#  value_3 = int(input("enter width: "))
#  value_4 = int(input("enter lenght: "))
#  print("The area of rectangle is: ",rectangle(value_3,value_4))
# else:
#   print("a is greater than b")


# def shape (h,b):
# # if(choice=='triangle'):
#  h = int(input("enter height: "))
#  b = int(input("enter base: "))
#  area = h*b/2
#  return (area)
#  shape(h,b)
#  print("The area of triangle is: ",shape(h,b))


#   h = int(input("enter height: "))
#  b = int(input("enter base: "))
#  def shape(h,b):
#     area = h*b/2
#     return(area)
#  shape(h,b)
#  print("The area of triangle is: ",shape(h,b))



 def character():
 names = input("Enter a list of names: ")
 users = names.split()                   #split() convert a string into list
 list = []
 max_len = -1
 lname = "";
 for  user in  users:
  if (len(user) > max_len):
    max_len = len(user)
    lname = user
    
 print (lname)
 print(len(user))


character()    