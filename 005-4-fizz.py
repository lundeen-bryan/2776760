"""
FizzBuzz Rules:
Counting from 1 to 100
for ea number divisible by 3 = fizz
for ea number divisible by 5 = buzz
display as:
1
2
fizz
4
buzz
etc
"""
for num in range(0, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0 and num % 5 != 0:
    print("Fizz")
  elif num % 3 != 0 and num % 5 == 0:
    print("Buzz")
  else:
    print(num)
