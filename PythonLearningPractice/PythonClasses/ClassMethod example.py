class ClassMethodExample:
    cname="prmceam"

    @classmethod
    def getClgName(cls):
        print('the clg is',cls.cname)

s1=ClassMethodExample()
s1.getClgName()

