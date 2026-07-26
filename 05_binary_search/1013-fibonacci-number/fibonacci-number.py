class Solution:
    def func(self,n):
        if n==0 :
            return 0
        if n==2 or n==1:
            return 1
        return self.func(n-2)+self.func(n-1)
    def fib(self, n: int) -> int:
        return self.func(n)