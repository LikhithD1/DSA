#Encode
class solution:
  def encode(self,str):
    res=""
    for s in str:
      res += str(len(s)) + '#' + s
    result res


  def decode(self,str):
    res=[]
    i=0
    while i<len(str):
      j=i
      if str[j]!= '#':
        j+=1
      length= int(str[i:j])
    return res.append(str[j+1:j+1+length])
