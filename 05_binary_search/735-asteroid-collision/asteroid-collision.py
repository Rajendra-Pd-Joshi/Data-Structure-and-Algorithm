class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            while len(stack) != 0 and stack[-1] > 0 and num < 0:
                # only one condition for collision
                sum = stack[-1] + num
                if sum > 0:
                    break
                elif sum < 0:
                    stack.pop()
                elif sum == 0:
                    stack.pop()
                    break
            else:
                stack.append(num)
        
        return stack
