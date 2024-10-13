def reverse_string(s):
 stack = []
 for char in s:
  stack.append(char)
  reversed_str = ''
 while stack:
  reversed_str += stack.pop()
 return reversed_str
input_string = "Python"
print("String yang dibalik:", reverse_string(input_string))