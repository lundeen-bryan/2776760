"""
x = [i for i in range(10)]
print(x)

x = [x**2 for x in range(10)]
print(x)

list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)

listOfWords = ['this','is','a','list','of','words']
items = [ word[0] for word in listOfWords ]
print(items)

x = [double(x) for x in range(10) if x%2==0]
print(x)
"""
with open("./src/026/01/file1.txt", 'r') as f:
  result1 = f.readlines()
print(f"Result1: {result1}")

with open("./src/026/01/file2.txt", 'r') as f:
  result2 = f.readlines()
print(f"Result2: {result2}")

result = [int(file) for file in result1 if file in result2]
print(result)

