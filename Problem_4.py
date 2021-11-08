def is_relation(A = [], R = []):
    list1 = []
    for i in A:
        for x in A:
            y = [i,x]
            list1.append(y)

    print(list1)
    #Checking is R is a set
    list2 = []
    lst =[]
    for r in R:
        if r not in lst:
            lst.append(r)
    if lst == R:
        print("R is a set")

    #Finding out if R is a relation of A*A
    for z in R:
        if z in list1 and z not in list2:
            list2.append(z)
        else:
            v = z
    if list2 == R:
        print("R is a relation on A")

        # Finding if R is reflexive or not
        r = []
        t =[]
        for i in R:
            for s in A:
                if i in list1 and i[0] == i[1] and i[0] == s:
                    r.append(i)
                    # print("check1", r)

                for k in r:
                    if s == k[0] and s not in t:
                        t.append(s)
                        # print("Check", t)
        t.sort()
        A.sort()
        if t == A:
            print("R is reflaxive ")
        else:
            print("R is not reflaxive")

        # Finding out if R is symmetric or not.
        list3 = []
        list4 =[]
        for l in R:
            if l[0] != l[1]:
                for o in R:
                    if l[0] == o[1] and l[1] == o[0] and l  not in list3 and o not in list3  :
                        # print("R is symmetric")
                        list3.append(o)
                        list3.append(l)
                list4.append(l)

        list3.sort()
        list4.sort()
        if list3 == list4:
            print("R is symmetric")
        else:
            for k in list4:
                if k not in list3:
                    print("R is not symmetric :", k)

        # Finding out if R is Transitive or not
        # Firstly we are going to loop through R
        for p in R:
            # We created a variable called trial that is initially empty. We will use it letter on
            trial = None
            # We looped through R again this time using u.
            for u in R:
                '''
                 We used one of the properties of a transitive i.e an element is transitive if [a,b],[b,c] then [a,c]
                 Firstly we compared our first and second variables (p and u) in terms of [a,b],[b,c]
                 then proceed to line 69
                '''
                if p[1] ==  u[0]:
                    """We then stored p[0] and u[1] (which is of the form [a,c] to variable x"""
                    x =[p[0],u[1]]
                    # We are going to find out if x exists in R
                    if x in R :
                        pass
                    else:
                        #If x is not in R we are going to append it to a list
                        trial = [p, u]

        # finding out if trial does not have any values
        if trial is None:
            print("R is transitive")
        else:
            print("R is not transitive : ", trial)

    else:
        print("R is not a subset of A because the following element is in R but not in A*A:",v, "R is not a relation of A")


A = [2, 1, 4, 6, 7, 3]
#R = [[2,4],[4,2],[2,2],[4,4],[1,4],[5,2]
R = [[2,4],[3,3],[1,1],[2,2],[7,7],[3,2],[6,6],[4,4],[2,3],[3,4],[4,2],[4,6],[6,4],[5,2]]
is_relation(A, R)
