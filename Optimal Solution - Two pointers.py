'''
Algorithm :
  Use two pointers: left and right to traverse the array.
  Track the last seen nonzero element in left pointer.
  If an opposite fort is found (forts[left] == -forts[right]), update the maximum captured forts.
  Update left to right for the next potential capture.
  Note: Guys dry run and do manual calculations for testcase forts -> forts = [1,0,0,-1,0,0,0,0,1] and you'll understand it better.
'''
def captureForts(self, forts):   #You should ignore the self parameter if you do not refer to any class instances guys, remember that.   
      left = ans = 0
      n = len(forts)
      for right in range(1, n) :
          if forts[right] :
              if forts[left] == -forts[right] :   
                  ans = max(ans, right-left-1)
              left = right
      return ans
'''
Time Complexity : O(n) 
Space Complexity : O(1) 
No extra space used.
'''
