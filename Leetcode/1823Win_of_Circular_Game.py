class Sultion:
    def findTheWinner(self, n: int, k:int) -> int:
        res = 0
        for i in range(2,n+1):
            res = (res+k)%i
        return res
    # another solution
    def topdown(self, n: int, k: int) -> int:
        if n == 1 : return 1
        else : return (self.topdown(n-1,k)+k -1)%n + 1 # to avoid index = 0
                                            #scale down, actually i don't know??

test = Sultion()
print(test.findTheWinner(128,64))
