#implicit type casting
x = 10 #int
y = 2.5 #float

sum = x + y #10.0 + 2.5 = 12.5
print("type of sum :",type(sum))

#exlpicit type casting
value = "100"#string
num = int(value)
print ("type of value:",type(num))

f=float(value)
print("type of f:",type(f))

price = 19.99
price_str = str(price)
print("price:",price_str)
print("type of price_str:",type(price))

