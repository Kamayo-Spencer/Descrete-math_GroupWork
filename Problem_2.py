# def truth_values(A = {}, B = {}):
#
#     list1 =[]
#     for i in B:
#         if i in A:
#
#             list1.append(i)
#     if list1 == B:
#         print(True, "Set B is a subset of set A")
#     else:
#         print(False,"Set B is not a subset of Set A")
#
#
#
#
# truth_values([1, 2,3,4,6,7 ,8], [5,1,3, 4,6])
def sets_functions(A, B):
    # Finding if B is a subset of  B
    x = B.issubset(A)

    # Finding the difference between A and B
    y = A.difference(B)
    # Returning the intersection of A and B
    z = A.intersection(B)

    # Returning the truth value of B subset A
    print(x)
    #Printing the difference between A and B
    print(y)
    #Printing the intersection of A and B
    print(z)


B = {"a", "b", "c"}
A = {"f", "e", "d", "c", "b", "a"}
sets_functions(A, B)

