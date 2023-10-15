import re 
  
  
print('negation:', re.search(r'n[^e]?', 'Python')) 
print('lookahead:', re.search(r'n(?!e)', 'Python')) 

print(re.search(r'[\d]{3,5}', '4444'))

print('Three Digit:', re.search(r'[\d]{3,4}', '189')) 

print(re.split(' ', 'Words, words , Words'))