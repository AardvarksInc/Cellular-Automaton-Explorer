def generate_conway_rule():
    rule = [0] * 512

    for i in range(512):
        config = format(i, "09b")

        neighbors = config[:4] + config[5:]
        live_neighbors = neighbors.count("1")

        if config[4] == "1" and live_neighbors in {2, 3}:
            rule[i] = 1
        elif config[4] == "0" and live_neighbors == 3:
            rule[i] = 1

    return rule


def generate_fib_rule():
    rule = {"1": "10", "0": "1"}
    string = "1"
    while len(string) <= 512:
        new_chars = []
        for char in string:
            new_chars.append(rule[char])
        string = "".join(new_chars)
    return string


print(generate_fib_rule())
