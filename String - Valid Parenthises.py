stack=[]
closedtoopen = { ')' :')' , ']' :'[' , '}':'{'}

for c in str:
  if c in  closedtoopen:
    if stack and stack[-1]==closedtoopen[c]:
      stack.pop()
    else:
      return False
  else:
    stack.append(c)
 return True if not stack else False   
