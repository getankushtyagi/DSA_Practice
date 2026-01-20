'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

'''


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or flowerbed[i - 1] == 0
                right_empty = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

                if left_empty and right_empty:
                    flowerbed[i] = 1   # plant flower
                    count += 1

                    if count >= n:
                        return True

        return count >= n
