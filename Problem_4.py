def is_relation(A = [], R = []):
    list1 = []
    for i in A:
        for x in A:
            y = [i,x]
            list1.append(y)

    print(list1)
    list2 = []
    for z in R:
        if z in list1:
            list2.append(z)
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
        #
        # [(2,4), (4,2)]
        for p in R:
            # if p[0] != p[1]:
            for u in R:
                if p[1] ==  u[0]:
                    for q in R:
                        # [(a,b),(b,c),(a,c)]
                        if q[0] == p[0] and q[1] == u[1]:
                            y1 = [p,u,q]
                            # print("R is transitive :", p, u, q)
                            # print(y1)
                        else:
                            y2 = [p,u,q]

                           # print("R is not transitive: ",p, u)

        if y1 == y2:
            print("R is transitive")
        else:
            print("R is not transitive :",y2[0], y2[1])
    else:
        print("R is not a relation of A")


A = [2, 1, 4, 6, 7, 3]
R = [[2,4],[3,3],[1,1],[2,2],[7,7],[3,2],[6,6],[4,4],[2,3],[3,4],[4,2],[4,6],[6,4]]
is_relation(A, R)
