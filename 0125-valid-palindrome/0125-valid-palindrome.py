class Solution:

  def isPalindrome(self, s: str) -> bool:
    s = [ch.lower() for ch in s if ch.isalnum()]
    ans = ""
    for i in range(len(s) - 1, -1, -1): 
      ans = ans + s[i]
    if ans == "".join(s):
      return True  
    else:
      return False 