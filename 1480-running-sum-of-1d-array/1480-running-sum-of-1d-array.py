class Solution:

  def runningSum(self, nums: List[int]) -> List[int]:
    ans = 0
    a = []
    for num in nums:
      ans += num
      a.append(ans)
    return a