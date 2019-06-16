# def greet():            #funtion definition
#     print('good morning')
# greet()                  #funtion calling
# print('i am outside the function')
# greet()

# a = int(input('enter 1st number'))
# b = int(input('enter 2nd number'))
# def add(num1 , num2): #recieving data called parameters
#     sum = num1 + num2
#     print(sum)
# add(a,b) #passing data (a and b called argument )2

# a = int(input('enter 1st number'))
# b = int(input('enter 2nd number'))
# opt = input('enter operation')
# if opt == "-":
#     def sub(num1 , num2): #recieving data called parameters
#         diff = num1 - num2
#         print(diff)
#     sub(a,b) #passing data (a and b called argument )2
# if opt == "*":
#     def mul(num1 , num2): #recieving data called parameters
#         product = num1 * num2
#         print(product)
#     mul(a,b) #passing data (a and b called argument )2
# if opt == "/":
#     def div(num1 , num2): #recieving data called parameters
#         divi = num1 / num2
#         print(divi)
#     div(a,b) #passing data (a and b called argument )2

#positional argumenmt passing
# def my_pet(owner , pet):
#     print(owner , " is a owner of ", pet)
# my_pet('cat' , 'sarah')

#key word argument passing
# def my_pet(owner , pet):
#     print(owner , " is a owner of ", pet)
# my_pet(pet='cat' , owner='sarah')

#default argument passing
# def my_pet(owner , pet, city = 'karachi'):
#      print(owner , " is a owner of ", pet, ".they are from ", city)
# my_pet(pet='cat' , owner='sarah' , city = 'lahore')

#takes nothing return something
# def sum():
#     b = 2
#     a = 3
#     #print('sum is' (a+b))
#     return(a+b)
# result =sum()
# print(result)

#takes something returns something
# a = int(input('enter 1st number'))
# b = int(input('enter 2nd number'))
# def sum(val1 ,val2):
#     result = val1 + val2
#     return result
# output_of_functon = sum(a,b)
# print(output_of_functon)

#class task: find if its even or odd
# a = int(input('enter 1st number'))
# def evod(num1):
#     if (num1%2) == 0:
#         return 'even'
#     else: 
#         return 'odd'
# result = evod(a)
# print('the given number is ', result)

# --------X----------X------------------X---------------X-----------------

# def pizza(crust , *topping): #ksi b variable se phly * lgadenge to multiple argument store kra skt in parameter
#     print('you have ordered the pizza with', crust, 'crust and following toppings')
#     for each in topping:
#         print(each)
# pizza('thick', 'olives','onions','chicken','cheese')


def pizza(crust , **topping): #ksi b variable se phly * lgadenge to multiple argument store kra skt in parameter
    print('you have ordered the pizza with', crust, 'crust and following toppings')
    for key in topping.keys():
        print(key)
pizza('thick', topping1 = 'olives' ,topping2 = 'onions' , topping3= 'chicken' , topping4 = 'cheese')

#topping = {topping1 = 'olives' ,topping2 = 'onions' , topping3= 'chicken' , topping4 = 'cheese'}