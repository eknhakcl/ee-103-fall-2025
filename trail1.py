my_num = input("Enter a number: ")
m = 0 
for n in range(len(my_num)):
    digit = int(n)
    #eğer n i int n e eşitlersek döngü başa sardığında çift index olarak algılar
    if digit % 2 ==0:
        m += int(my_num[n])
        print(my_num)
print(m)