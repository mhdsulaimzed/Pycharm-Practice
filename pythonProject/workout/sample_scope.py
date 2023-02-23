def check_scope():
    def do_global():
        global test
        test = "global test"


    def do_local():
        test = "local tst"


    def do_nonlocal():
        nonlocal test
        test = "non local tst"

    test="default"
    do_local()
    print(test)
    do_nonlocal()
    print(test)
    do_global()
    print(test)

check_scope()
print(test)