def main():
    #Q1
    out_file = open("name.txt", "w")
    name = input("Please enter name:")
    print("{}".format(name), file=out_file)
    out_file.close()

    #Q2
    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    in_file.close()
    print("Your name is {} ".format(name))

    #Q3
    in_file = open("numbers.txt", "r")
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    in_file.close()
    print(number1 + number2)

    #Q4
    in_file = open("numbers.txt", "r")
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    in_file.close()
    print(total)


main()