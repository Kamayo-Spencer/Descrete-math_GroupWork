def truth_value(X =[], Y =[]):
    for i in Y:
        for j in X:
           if j%i == 0:
               print("True")
           else:
               print("False")

X = [10,20,30,40]
Y = [3,4,8,10]
truth_value(X,Y)

