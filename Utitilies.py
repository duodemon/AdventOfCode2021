def parse(filename):
    input_array = []
    f = open(filename, "r")
    if f is not None:
        input_string = f.read()
        input_array = input_string.split("\n")
        return input_array
