#lower
original = "hello world"
lowered = original.lower()
print("lowercase:",lowered)

#upper method
uppered = original.upper()
print("uppercase:",uppered)

#strip() method
messy = "python"
cleaned = messy.lower()
print("after strip:",cleaned)

#replace() method
text ="java is powerful"
updated = text.replace("java","python")
print("after replaced:",updated)

#split() method
sentence = "python is easy to learn"
words = sentence.split()
print("split words:",words)

#find() method
text = "learning python is fun"
position = text.find("python")
print("found at index:",position)

#title() method
heading = "welcome to python programming"
formatted = heading.title()

#capitalize() method
msg = "hello world"
cleaned = msg.capitalize()
print("capitalize:",cleaned)

#startswith() method
print("hello everyone")
print("greeting.startswith('hello')")
print("greeting.startswith('hi')")

#endswith() method
print("greeting.endswith('everyone')")
print("greeting.endswith('hello')")

#count() method
sentence = "python is easy.Python is powerful.Python is fun"
count = sentence.count("python")
print("total count:",count)

#isolation() method
name = "PYTHON"
print(name.isalpha())