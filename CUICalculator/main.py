""" CUI Calculator 
"""

import msvcrt
from os import system, name

# Prints a line
def print_line():
    print("--------------------------------------------------")


# Clear keyboard buffer
def flush_input():

    # for windows
    if name == "nt":
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()

    # for linux/unix
    else:
        import sys, termios

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


# Clear the screen
def clear_screen():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


# Take keyboard input
def keyboard_input(rng) -> int:
    # for windows
    while True:
        _char = msvcrt.getch()
        try:
            _char = int(_char)
        except ValueError:
            continue

        if _char in rng:
            return _char


class Arithmetic_Switch:
    def __init__(self):
        flush_input()
        clear_screen()
        print(
            "\t\tCALCULATOR (Arithmetic)\n[0] Back\n[1] Add\t[2] Multiply\n[3] Subtract\t[4] Divide\n(give multiple input separated by space)\n"
        )
        print_line()

        opt = keyboard_input(range(0, 5))
        self.switch(opt)

    def main(self):
        flush_input()
        opt = keyboard_input(range(0, 5))
        self.switch(opt)

    def switch(self, opt):

        default = "Unkonwn Operation"

        return getattr(self, "case_" + str(opt), lambda: default)()

    def case_0(self):
        Main_Switch()

    def case_1(self):
        print("SUM\n")

        num = input("> ").split(" ")
        num = list(map(int, num))

        print("\nRESULT:", sum(num))
        print_line()

        self.main()

    def case_2(self):
        print("PRODUCT\n")
        num = input("> ").split(" ")
        num = list(map(int, num))
        x = num[0]
        for n in num[1:]:
            x *= n

        print("\nRESULT:", x)
        print_line()

        self.main()

    def case_3(self):
        print("DIFFERENCE\n")

        num1 = int(input("n1> "))
        num2 = int(input("n2> "))

        print("\nRESULT:", num1 - num2)
        print_line()

        self.main()

    def case_4(self):
        print("QUOTIENT\n")

        num1 = int(input("n1> "))
        num2 = int(input("n2> "))

        print("\nRESULT:", num1 / num2)
        print_line()

        self.main()


class Main_Switch:
    def __init__(self):
        flush_input()
        clear_screen()
        print("\t\tCALCULATOR\n[0] Exit\t[1] Arithemetic\n[2] Equaiton\t[3] Functions")
        opt = keyboard_input(range(0, 4))
        self.switch(opt)

    def switch(self, opt):

        default = "Unkonwn Operation"

        return getattr(self, "case_" + str(opt), lambda: default)()

    def case_0(self):
        exit(0)

    def case_1(self):
        Arithmetic_Switch()

    def case_2(self):
        print("case 1")

    def case_3(self):
        print("case 1")


if __name__ == "__main__":
    Main_Switch()
