class DataTypes:
    from builtins import print
#
    class DataTypes:
        #int data
        intx, intc, intx, intsd = 10, 22, 54, 54
        print(intx, intc, intx, intsd)

        # bytes datatype
        v = [10, 20, 30, 25, 255]
        b = bytes(v)
        for x in b: print(x)


        # btyearray datatypes
        b = [10, 22, 32, 5, 5]
        k = bytearray(b)
        b[0] = 99
        for b in k: print(b)


        # set datatype

        thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
        print(thisset)
        pass


        #list datatype

        thislist=['vinay','raj','lokesh',12,'ram','333']
        print(thislist)
        thislist[0:2]
        thislist.append('vaishav')
        thislist.remove('raj')
        for i in thislist:print(i)