def parse(filename, delimiter="\n"):
    f = open(filename, "r")
    if f is not None:
        input_string = f.read()
        input_array = input_string.split(delimiter)
        return input_array
