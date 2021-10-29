def list_functions(A = [], B = [] ):
    list1 = []
    for i in B:
        if i in A:
            list1.append(i)
    if list1 == B:
        print("B is a subset of A")
    else:
        print("B is not a subset of A")

def list_difference(A, B):
    list2 = []
    for i in A:
        if i in B:
            pass
        else:
            list2.append(i)
    print("Printing the difference between A and B")
    print(list2)
def list_multiplication(A, B):
    list3 = []
    for i in A:
        for x in B:
            y = [i, x]
            list3.append(y)


    print(list3)


A = ["Marion", "Nahashon", "Petronalla", "Abot", "Spencer"]
B = ["Marion", "Nahashon", "Kamayo"]
list_functions(A, B)
list_difference(A, B)
list_multiplication(A, B)