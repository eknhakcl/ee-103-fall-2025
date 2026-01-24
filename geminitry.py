class Book():
    def __init__(self,page):
        self.page = page

    def __len__ (self):
        return self.page
    
print(len(Book(300)))


class sayi():
    def __init__(self,value):
        self.value = value

    def increase(self):
        self.value +=1
c = sayi(5)
c.increase()
print(c.value)