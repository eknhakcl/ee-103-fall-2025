# def countdown(n):
#     if n < 0:
#         return n
#     else:
#         print(n)
#         countdown(n - 1)
#         return 
    
# print(countdown(5))

########################################################

# def liste_top(liste):
#     total = 0
#     if len(liste) == 0: 
#         return 0 
#     else:
#         return liste[0] + liste_top(liste[1:])
    

# print(liste_top([20,30,40,50,60]))


#######################################################

# def ters_cevirme(word):
#     if len (word) == 0:
#         return ""
#     else:
#         return word[-1] + ters_cevirme(word[:-1])
    
# print(ters_cevirme("yeteeeeeeeeer"))

########################################################   

def duzlestirme(liste):
    son_liste = []
    for i in liste:
        if isinstance(i, list):
            son_liste.extend(duzlestirme(i))
        else:
            son_liste.append(i)
    return son_liste

print(duzlestirme([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))