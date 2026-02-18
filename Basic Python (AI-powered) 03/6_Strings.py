# Strings
name = "Adil"
print(name)

#String Length
text = "Python"
length = len(text)

#Accessing Characters in a String
text = "Python"
print(text[0])
print(text[3])

#String Slicing
text = "Python"
print(text[0:3])
print(text[2:])
print(text[:4])

#String Methods lower() and upper()
text = "Python"
print(text.lower())
print(text.upper())

#strip() :> Removes leading and trailing whitespace from a string.
text = "  hello  "
print(text.strip())

#replace() :> Replaces occurrences of a specified substring with another substring.
text = "Hello World"
print(text.replace("World", "Python"))

#split() :> Splits a string into a list of substrings based on a specified delimiter.
text = "apple,banana,orange"
items = text.split(",")
print(items)

#join() :> Joins a list of strings into a single string using a specified delimiter.
items = ["apple", "banana", "orange"]
text = ", ".join(items)
print(text)

#find() :> Returns the index of the first occurrence of a specified substring in a string. If the substring is not found, it returns -1.
text = "Hello World"
index = text.find("World")
print(index)

#find() with a substring that is not present
text = "Hello World"
position = text.find("World")
print(position) 

#startswith() and endswith() :> These methods check if a string starts or ends with a specified substring, respectively, and return True or False.
email = "test@gmail.com"

print(email.startswith("test"))
print(email.endswith(".com"))

#String Concatenation
first = "Hello"
second = "World"

result = first + " " + second
print(result)

#String Formatting using f-strings
name = "Harry"
age = 25

message = f"My name is {name} and I am {age} years old"
print(message)

#Checking String Content with isalpha() and isdigit()
text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

# #Strings are Immutable 
# text = "Python"
# text[0] = "J"
# print(text)

#String Immutability workaround
text = "Python"
new_text = "J" + text[1:]
print(new_text)
