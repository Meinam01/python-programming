#basic function
def greet():
    print("welcome to python functions!")

greet()
greet()
greet()

#2. greeting with name
def greet_user(name):
    print("hello,",name)

greet_user("ramesh")
greet_user("raj")
greet_user("salman")

#square function
def square(num):
    return num*num

result = square(6)
print("square:",result)
print(square(10))
print(square(100))
def get_max(a , b):
   if a > b:
      return a
   else:
      return b

max_value = get_max(40, 30)
print("maximum:",max_value)

#calling function inside a loop
def greet_user(name):
    print("hello," +  name + "!")

names = ["alice","bob","charlie"]
for name in names:
    greet_user(name)

#functions with default value - Ex.guest
def greet_default(name="guest"):
    print("hello",name)
greet_default()
greet_default("ravi")