# problem 1

def sum_to(n):
  sum = 0
  for num in range(1, n + 1):
    sum += num
  return sum
print(sum_to(6))


# problem 2

def largest(list):
  list.sort()
  return list[-1]

print(largest([3, 5, 2, 1, 3]))

# problem 3

def occurances(str1, str2):
  num = str1.count(str2)
  return num

print(occurances("beep boop", "b"))

# problem 4

