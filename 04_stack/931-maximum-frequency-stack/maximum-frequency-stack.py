class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stack = defaultdict(list)
        self.maxcnt = 0

    def push(self, val: int) -> None:
        self.cnt[val] +=1
        freq = self.cnt[val]
        
        self.maxcnt = max(self.maxcnt,freq)

        self.stack[freq].append(val)

    def pop(self) -> int:
        
        ans = self.stack[self.maxcnt].pop()
        self.cnt[ans] -=1
        if not self.stack[self.maxcnt]:
            self.maxcnt -=1

        return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()