# We are defining a function that  gets a list as an input.
def checking_sets(list1= []):
    #We are going to first sort the list into an ascending order for easy manipulation
    list1.sort()
    # Converting the list into a set
    list2 = set(list1)
    # Converting list2 back to a list so that we can compare it with list1
    list2 = list(list2)
    # Sorting list2 into ascending order
    list2.sort()
    # Comparing list1 to list2  and printing true if they are the same and false if otherwise
    if list1 == list2:
        print("True")
    else:
        print("False", "the set should be :", list2)


checking_sets([1, 2, 23,44, 5, 66,1])
# ["Spencer", "Nahashon", "Abot", "Petronalla", "Marion", "Trees"]