'''
Given arrival arr[] and departure dep[] times of trains on the same day, find the minimum number of platforms needed so that no train waits. A platform cannot serve two trains at the same time; if a train arrives before another departs, an extra platform is needed.

Note: Time intervals are in the 24-hour format (HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

Examples:

Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3
Explanation: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.

'''

class solution:
    def platform(self,arr,dep):
        n=len(arr)
        
        arr.sort()
        dep.sort()
        
        max_platform=1
        platform_req=1
        
        i=1
        j=0
        while i<n and j<n:
            if(arr[i] <= dep[j]):
                platform_req+=1
                max_platform=max(platform_req,max_platform)
                i+=1
            else:
                platform_req-=1
                j+=1
        return max_platform
    
    
obj=solution()
print(obj.platform(arr = [900, 940, 950, 1100, 1500, 1800], dep = [910, 1200, 1120, 1130, 1900, 2000]))
            
        
        