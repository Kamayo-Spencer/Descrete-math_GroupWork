# Creating a function that accepts two lists as inputs
def truth_value(X=[], Y=[]):
    # A variable var that is initially 0 and would increment when a y that divides an X is found
    val = 0
    # looping through list X and Y and finding the modulus
    for i in Y:
        for j in X:
            if j % i == 0:
                val += 1

        # setting val to 0 if condition is met
        if val != len(X):
            val = 0
        else:
            print("True")
            break
    # Printing false if the condition is not met
    if val != len(X):
        print(False)


X = [10, 20, 30, 40]
Y = [3, 7, 9, 180]
truth_value(X, Y)
