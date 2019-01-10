def my_func_test():
    assert my_run("How are you :-) doing :-( today :-)?") == "happy"
    assert my_run(":)") == "none"
    assert my_run("This:-(is str:-(:-(ange te:-)xt.") == "sad"


def my_run(my_str):
    h = my_str.count(":-)")
    s = my_str.count(":-(")
    if h == 0 and s == 0:
        return "none"
    elif h > s:
        return "happy"
    elif h == s:
        return "unsure"
    else:
        return "sad"


my_func_test()
