class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids :
            while stack and stack[-1]>0 and num<0:
                # only case for collision
                sum = stack[-1] + num
                if sum > 0:
                    break
                elif sum < 0:
                    stack.pop()
                else:
                    stack.pop()
                    break
            else:
                stack.append(num)
        return stack