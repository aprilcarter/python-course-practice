def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            newargs = []
            for (arg, type) in zip(args, types):
                newargs.append(type(arg))
            return f(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)
