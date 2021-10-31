def truth_value(X =[], Y =[]):
    for i in Y:
        for j in X:
           if j%i == 0:
               return True
           else:
               return False

X = [10,20,30,40]
Y = [2,4,8,10]
print(truth_value(X,Y))

