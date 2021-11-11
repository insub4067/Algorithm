def convert_to_int(x):
    if type(x) == float or type(x) == int:
        return x
    if "k" in x:
        if len(x) > 1:
            return float(x.replace("k", "")) * 1000
        return 1000.0
    return 0.0


# if x is '1.1k' def return 1100
