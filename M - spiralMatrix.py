res=[]
left,right=0,len(martix[0])
top,bottom=0,len(martrix)
while left <right and top < buttom:
  for i in range (left,right):
    res.append(martix[top][i])
  top +=1
   for i in range (top,buttom):
    res.append(martix[i][right-1])
   right -=1
  if not (left < right and top < buttom):
    break
   for i in range (right-1,left-1,-1):
    res.append(martix[bottom-1][i])
   buttom -=1
   for i in range (buttom-1,top-1,-1):
    res.append(martix[i][left])
  left +=1
 return res 
