total_used = 1

def total(a1, b1):
    return a1+b1

def difference(a1, b1):
    return a1 - b1


class Mylogic:
    used = 0
    def total(self, a1, b1):
        self.used = self.used + 1
        return a1+b1
    def getUsed(self):
        return self.used
    def difference(self,a1,b1):
        return a1-b1
