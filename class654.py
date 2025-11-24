# def create_list(a):
#     range_list = list(range(a))
#     return range_list

# a = int(input("Enter a number: "))
# result = create_list(a)
# print(f"List from 0 to {a-1}: {result}")

############################################

# def triangular_number(n):
#     x =1
#     empty_list = []
#     while x<=n :
#         triangular_num = (x*(x+1))//2
#         empty_list.append(triangular_num)
#         x+=1    
#     return empty_list


# n = int(input("Enter a number: "))
# result = triangular_number(n)   
# print(result)

#############################################

# def is_tri(num):
#     is_triangular = False
#     x = 0
#     for i in range(0,num+1):
#         x += i
#         if x == num:
#             is_triangular = True
#             break   

#     return is_triangular


# num = int(input("Enter a number: "))
# result = is_tri(num)
# print(result)

#############################################

def sum_sq(n1, n2):
    sq_list = []
    while n1 <= (n2+n1):
        sq = n1 ** 2
        sq_list.append(sq)
        n1 += 1
    sq_list = sum(sq_list)
    return sq_list

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
result = sum_sq(n1, n2)
print(result)
