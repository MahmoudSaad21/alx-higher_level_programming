def safe_print_list(my_list=[], x=0):
    try:
        c = 0
        for i in my_list:
            if c < x:
                print(i, end = "")
                c=c+1
        print()
        return c
    except:
        c = 0
        for i in my_list:
            print(i, end = "h")
            c=c+1
        print()
        return c
