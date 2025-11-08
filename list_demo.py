my_list = ["apple", "banana", "cherry"]
print(my_list)

numbers = [10,20,30,40]
print(numbers)

#mixed data types
mixed = ["hello",99,3,14,True]
print(mixed)

#empty list
empty_list=[]
print(len(empty_list))

#accessing elements from list - indexing
fruits = ["apple", "banana", "cherry","mango"]

#access first item
first_fruit = fruits[0]
print("first item: ",first_fruit)

third_fruit = fruits[2]
print("third item: ",third_fruit)

last_item = fruits[2]
print("last item: ",last_item)

#access last item using negative index
last_item_alt = fruits[-1]
print("last item using a negative index:",last_item_alt )

#updating list items
fruits = ["apple", "banana", "cherry","mango"]

fruits[1] = "blueberry"
print(fruits)

fruits[-1] = "kiwi"
print(fruits)

fruits[0] = "grape"
print(fruits)

#adding items to a list

#create empty list
fruits = []

#append method
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)

#insert method
fruits.insert(1,"orange")
print(fruits)

#extend method
fruits.extend(["mango","kiwi"])
print(fruits)


