def makeDict():
    name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
    favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
    new_list = zip(name,favorite_animal)
    # print len(name)
    # print len(favorite_animal)
    if len(name)>len(favorite_animal):
        new_list = zip(favorite_animal,name)
    else:
        new_list = zip(name,favorite_animal)
    new_dict=dict(new_list)
    print new_dict
makeDict()