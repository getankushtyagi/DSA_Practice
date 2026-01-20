'''
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

'''

# e.g [3,5,-6,2,-1,4]​​​​​​​

class Solution:
    def asteroidCollision(self, arr):
                
        stack=[]
        n=len(arr)
        
        for i in range(0,n):
            if(arr[i]>0):
                stack.append(arr[i])
            else:
                while len(stack) != 0 and stack[-1]> 0 and stack[-1]< abs(arr[i]):
                    stack.pop()

                if(len(stack) and abs(arr[i])==stack[-1]):
                    stack.pop()
                elif(len(stack) == 0 or stack[-1]< 0):
                    stack.append(arr[i])
            
        return stack
        
                
obj=Solution()
print(obj.asteroidCollision([3,5,-6,2,-1,4]))
            