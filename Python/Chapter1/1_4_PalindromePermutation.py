#O(N)

def permPal(s):
  s = s.lower()
  char_set = [0 for i in range(26)]
  countOdd = 0
  
  for char in s:
    x = char_num(char)
    
    if x != -1:
      char_set[x] += 1
    
      if char_set[x] % 2 == 1:
        countOdd += 1
      else:
        countOdd -= 1
    
  return countOdd <= 1

def char_num(c):
  a = ord('a')
  z = ord('z')
  val = ord(c)
  
  if a <= val <= z:
    return val - a
  else:
    return -1
    

print(permPal('Tact Coa'))
