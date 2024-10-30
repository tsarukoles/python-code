# Task_425

size = 9
stars = 0
spaces = 0
center = size // 2
choice = input("What figure do you want to display:\n Figure A\n Figure B\n Figure C\n Figure D\n Figure E\n Figure "
               "F\n Figure G\n Figure H\n Figure I\n Figure J\n For exit type: X\n")
while choice != "X":
    if choice == "A":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    spaces = i
                    stars = size - i - 1
            print(" " * spaces + "*" * stars)
    if choice == "B":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    stars = i
                    spaces = size - i - 1
            print("*" * stars + " " * spaces)
    if choice == "C":
        for i in range(size):
            for j in range(size, 0, -1):
                if i <= size:
                    stars = size - i - spaces
                    spaces = i
            print(" " * spaces + "*" * stars + " " * spaces)
    if choice == "D":
        for i in range(size, -1, -1):
            for j in range(size):
                if i <= size:
                    stars = size - i - spaces
                    spaces = i
            print(" " * spaces + "*" * stars + " " * spaces)
    if choice == "E":
        for i in range(size):
            for j in range(size):
                if i < center:
                    stars = size - i - spaces
                    spaces = i
                elif i > center and j > 5 or j < 9:
                    stars = 2 * (i - center) + 1
                    spaces = size - i - 1
            print(" " * spaces + "*" * stars + " " * spaces)
    if choice == "F":
        for i in range(size):
            for j in range(size):
                if i < center:
                    spaces = size - i - stars
                    stars = i
                elif i > center and j > 5 or j < 9:
                    spaces = 2 * (i - center) + 1
                    stars = size - i - 1
            print("*" * stars + " " * spaces + "*" * stars)
    if choice == "G":
        for i in range(size):
            for j in range(size):
                if i < center:
                    spaces = size - i - stars
                    stars = i
                elif i > center and j > 5 or j < 9:
                    spaces = 2 * (i - center) + 1
                    stars = size - i - 1
            print("*" * stars + " " * spaces)
    if choice == "H":
        for i in range(size):
            for j in range(size):
                if i < center:
                    spaces = size - i
                    stars = i
                elif i > center and j > 5 or j < 9:
                    spaces = i + 1
                    stars = size - i - 1
            print(" " * spaces + "*" * stars)
    if choice == "I":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    stars = size - i - 1
                    spaces = i
            print("*" * stars + " " * spaces)
    if choice == "J":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    spaces = size - i - 1
                    stars = i
            print(" " * spaces + "*" * stars)

    choise = input(
        "What figure do you want to display:\n Figure A\n Figure B\n Figure C\n Figure D\n Figure E\n Figure F\n "
        "Figure G\n Figure H\n Figure I\n Figure J\n For exit type: X\n")