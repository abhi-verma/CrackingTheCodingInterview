# O(N)

def perm(str1, str2):
  if len(str1) != len(str2):
    return False
  
  d = {}
  
  for char in str1:
    if char in d:
      d[char] += 1
      
    else:
      d[char] = 1
      
  for char in str2:
    if d[char] == 0:
      return False
    else:
      d[char] -= 1
  
  return True
      
      
print(perm('abhinav', 'abhivan'))
