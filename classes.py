#class aslında list() yada str() gibi herhangi bir oluşturulmuş fonksiyonun kendimizin yaptığı halidir.
# class Person():
#     def __init__(self) :
#         #__init__: initilazer yani bu sınıf çağrıldığında ne yapılacağını söylüo
#         print("init")


class Person():
    #özellikler ama pythonda çokta gerekli değil bu şekilde yazılması direk fonskiyonda kullanılabilir
    name = ""
    age = 0
    gender = ""

    #initlilazer
    def __init__(self,name , age, gender):
        #artık isim yaş ve cinsiyrt yazmadan program çalışytırılamaz çünkü fonk tanımlanması için bu bilgilere ihtiyacı var.
        self.name = name
        self.age = age
        self.gender = gender
        #self: classlardaki fonskiyoların class için kullanılmasını sağlar.
        #Mesela burada Person() içindeki parametreleri __init__ fonksiyonun içinde eşitlemek için kullanılmış.
    #özellikler başta yazılmasa bile self.name tarzındaki yazılarla bu sınıfın name diye özelliği olucağı anlaşılır

    def info(self):
        return f"This persons name is {self.name} {self.age} years old and {self.gender}"

#her zaman fonksiyona ihtiyaç duymayabiliriz bazen sadece self. ilede bsait bir şekilde fonksiyon elde edebiliriz
#self.name = Person.name ama genelde self kullanılır

#####################################################################################################################
##INHERITENCE##

#bir classı başka bir classın içinde çalıştırma

class Employee(Person):

    def __init__ (self,name,age,gender):
        Person.__init__(self,name,age,gender)
    #aldığımız class ın initin içindekileri almazsak ordaki özellikler çalışmaz
    #bu şekilde belirtikten sonra bütün fonksiyonlar gelir
    #bunu kullandığımızda classın içine yeni fonksiyonlarda yazılabilir yada diğer classtan gelen fonksiyonlar değiştirelerekte yazılabilir
    
    def info(self):
        return f"This employee's name is {self.name} {self.age} years old and {self.gender}"

#####################################################################################################################
##POLYMORPHISM##

# farklı classlarda aynı isimli fonksiyonun olması ve bunların aynı anda çalıştırılabilmesi(for loopla örnek olarak)
ece = Person("Ece",26,"female")
ahmet = Employee("Ahmet",32,"male")
human_list = [ece,ahmet]
for human in human_list :
    print(human.info())

#####################################################################################################################
##ENCAPSULATION## (hapsetmek)

#classta input olarak girilen şeyi bir daha panelden değişitirlmemesi için kullanılaır
#tanımlarken self.__{tanımlanan şey} olarak yazılırsa artık sadece bu classın içinden değiştirilebilir


#####################################################################################################################
##ABSTRACTION##

#gizli class oluşturmak için kullanılır

from abc import ABC , abstractmethod

class Car(ABC):

    @abstractmethod
    def max_speed(self):
        pass

class Tesla(Car):

    def max_speed(self):
        return"200"
    
#Teslanın içine car yazdıktan sonra Car daki fonskiyon kulanılmak zorundadır oksa hata verir
#####################################################################################################################

#__str__ : classla oluşturulan obje direk printlenirken söylenilcek şeyi gösterir
#__(komut)__:herhengi bir komutu class içinde çağrıldığı zaman ne yapması gerektiğini manipüle edilebilir   


class Fruit():

    def __init__ (self,name, calorie):
        self.name=name
        self.calorie = calorie

    def __str__ (self):
        return f"{self.name}'s is {self.calorie} calorie."
    
    def __len__ (self):
        return len(self.name)
    
    def __getitem__(self , key):
        if key == str :
            return f"{self.name}?"
        else:
            return f"Ne dion cano?"
        
        
    