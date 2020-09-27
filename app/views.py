def testing(qstring):
    try:
        qlist = qstring.split("&")
        for q in qlist:
            key, value = q.split("=")
            if "test" == key:
                return "Testing value = {}".format(value)
        return "test"

    # retstr = 
    except:
        return "test"