def kansu(a, *args, **kwargs):
    print(a, type(a))
    print(args, type(args))
    print(kwargs, type(kwargs))

kansu(1)
kansu("a")
kansu(1,2,3,4)
kansu("a","b","c","d")
kansu(1, x="x", y="y", z="z")
kansu(1,2,3,4,x="x",y="y",z="z")