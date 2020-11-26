def string_analiz(a1,b1):
    #print(type(a1))
    if type(a1) == type(b1) and type(b1)==type(" "):
        #print("good")
        if len(a1) ==len(b1):
            return 1
        elif len(a1)>len(b1):
            return 2

        elif b1 =='learn':
            return 3
        else:
            pass
    else:
        #print(ValueError("dont string"))
        return 0

    #pass
#print(type("sd"))
print(string_analiz("fer","learn"))
print(string_analiz("fer111","learn"))
print(string_analiz("111","111"))
print(string_analiz(111,"111"))
