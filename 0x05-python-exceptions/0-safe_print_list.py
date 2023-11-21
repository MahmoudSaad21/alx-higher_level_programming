def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            print(i, endl = "")
        print()
        return x
    except:
        c = 0
        for i in my_list:
            print(i, endl = "")
            c=c+1
        print()
        return c
