class Solution:
  def palindrome(self,s:str)->bool:
    newstr=""
    for c in s:
      if c.isalnum():
        newstr += c.lower()
     return newstr == newstr[::-1]



###Method 2
class Solution:
  def palindrome(self,s:str)->bool:
    l,r=0,len(s)-1
    while l<r:
        while l<r  and not self.alphanum(s[l]):
          l+=1
        
         while r>l  and not self.alphanum(s[r]):
          r==1

         if s[l].lower() != s[r].lower():
          return False
           
         l,r = l+1,r-1
     return True 

  def alphanum(self,c):
    return(ord('A') <= ord(c) <=ord('Z') or 
           ord('a') <= ord(c) <=ord('z') or 
           ord('0') <= ord(c) <=ord('9')) 
    
  
