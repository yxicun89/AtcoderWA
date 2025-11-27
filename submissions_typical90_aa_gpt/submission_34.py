n = int(input())
hash_value = 8747
hash_list = [True] * hash_value

def char_to_int(char):
    if char.isdigit():
        return int(char)
    elif char.islower():
        return ord(char) - ord('a') + 1
    elif char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return 0

def sum_of_digits_and_letters(string):
    return sum(char_to_int(char) for char in string)

def hash_func(k, h):
  return k % h

for i in range(n):
  s = input()
  if hash_list[hash_func(sum_of_digits_and_letters(s), hash_value)] == False:
    continue
  else:
    hash_list[hash_func(sum_of_digits_and_letters(s), hash_value)] = False
    print(i+1)
    