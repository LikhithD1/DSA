l,r=0,len(martix)-1
while l<r:
  for i in range of (r-l):
    t,b=l,r
    new = martix[t][l+i]
    martix[t][l+i]=martix[b-i][l]
    martix[b-i][l]=martix[b][r-i]
    martix[b][r-i]=martix[t+i][r]
    martix[t+i][r]=new
  r-=1
  l+=1
