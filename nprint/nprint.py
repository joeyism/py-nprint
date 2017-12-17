import gc

def nprint(*args, **kwargs):
    nest = "\t"

    # Change what each nest is
    try:
        nest = kwargs["nest"]
        del kwargs["nest"]
        gc.collect()
    except:
        pass

    # Indent based on level
    try:
        level = kwargs["level"]
        del kwargs["level"]

        if level == 0:
            pass
        else:
            indents = "".join([nest for i in range(level)])
            largs = list(args)
            largs.insert(0, indents)
            args = tuple(largs)
            del largs, indents
            gc.collect()
    except:
        pass

    print(*args, **kwargs)
