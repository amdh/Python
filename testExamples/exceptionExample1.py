def greet_person(sPersonName):
    """
    says hello
    """
    if sPersonName == "Robert":
        raise Exception("we don't like you, Robert")
    print "Hi there {0}".format(sPersonName)



greet_person("amruta")
greet_person("Robert")