# def count_down(n):
#     if n == 0 :
#         return print(0)
#     else : 
#         print(n)
#         return count_down(n-1)
    

# count_down(3)
 ################################################################

class student :
    def __init__(self, name ):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

ogrenci1 = student ("Ekin")
ogrenci1.say_hello()