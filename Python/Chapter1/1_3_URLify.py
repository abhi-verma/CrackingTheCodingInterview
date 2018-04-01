# O(N)

def urlify(string, length):
    newIndex = len(string)
    
    for i in reversed(range(length)):
      if string[i] == ' ':
        # Replace spaces with %20
        string[newIndex - 3:  newIndex] = '%20'
        newIndex -= 3
      else:
        # Move characters
        string[newIndex-1] = string[i]
        newIndex -= 1
    
    return ''.join(string)
      
print(urlify(list('Mr John Smith    '), 13))
