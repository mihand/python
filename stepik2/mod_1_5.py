class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity #свободное место в копилке

    def can_add(self,v):
        if self.capacity - v >= 0:
            return True
        else:
             return False

    def add(self, v):
        if  self.can_add(v):
            self.capacity -= v

mb = MoneyBox(12)
print(mb.capacity)
for i in range(10):
    if mb.capacity <= 0: break
    print('добавляю {0} рублей'.format(i+1))
    mb.add(i+1)
    print('свободное место',mb.capacity)