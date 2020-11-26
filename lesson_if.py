


def age(a):
    b=a
    #print(a)

    if 6<b<9:
        print("kindergarten",b)
    elif 9<b<18:
        print("school",b)
    elif 18<b<23:
        print("institu",b)
    else:
        print("work",b)

a=int(input("vesti age \n"))
age(a)
