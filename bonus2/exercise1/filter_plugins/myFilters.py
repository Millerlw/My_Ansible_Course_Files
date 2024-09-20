def Moe(my_str):
    return my_str.upper()


def Larry(my_str):
    return my_str.lower()

def Curly(my_str):
    return my_str.capitalize()

class FilterModule(object):
    def filters(self):
        return {
            "moe": Moe,
            "larry": Larry,
            "curly": Curly,
        }
