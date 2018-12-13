def func():
    r = range(4)
    for i in r:
        yield r[i] + 10
        print("passed yield %s" % i)

def test_func():
    gen = func()
    print("gen: {}".format(gen))
    print("Calling next")
    val = next(gen)
    print("gen val: %d " % val)
    print("Calling next")
    val = next(gen)
    print("gen val: %d " % val)
    print("Calling next")
    val = next(gen)
    print("gen val: %d " % val)
    print("This is the end")

