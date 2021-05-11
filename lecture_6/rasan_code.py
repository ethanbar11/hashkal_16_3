with open(r"hello.txt") as f:

    with open(r"out.txt", "w") as f1:
        for line in f:
                f1.write(line)

        f1.write("\nadd")