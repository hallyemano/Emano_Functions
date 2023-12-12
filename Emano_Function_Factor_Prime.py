def smallestFactor():
    while True:
        n = int(input("\nEnter an integer greater than 2: "))

        if n < 2:
            print("Invalid input. Enter a number greater than 2.")
            break

        for i in range(2, n):
            if n % i == 0:
                print(f"The smallest factor other than 1 for {n} is: {i}")
                break
        else:
            print(f"{n} is a prime number.")

def PrimeNumber():
    print("\nRULES TO CONSIDER:")
    print("[1] If number[start] is a negative number, The program will promt a message: Enter a non-negative number.")
    print("[2] If number[end] is less than number[start]. The program will promt a message: Enter a Greater number than number[start].")
    print("[3] If the user enter the number 0, the program will terminate.")

    while True:
        first = int(input("\nEnter a number [start]: "))

        if first == 0:
            print("Program Terminated.")
            break

        if first < 0:
            print("Enter a non-negative number.")
            continue

        last = int(input("Enter a number [end]: "))

        if last <= first:
            print(f"Enter a number greater than {first}.")
            continue

        print(f"Prime numbers between {first} to {last} are: ", end=" ")

        for n in range(first, last + 1):
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        break
                else:
                    print(n, end=" ")

        print()

def main():
    while True:
        print("\nRULES TO CONSIDER:")
        print("[1] If the user selects 1, the code for  finding the smallest factor of n will invoked.")
        print("[2] If the user selects 2, the code for  finding the prime numbers of range will invoked.")

        choice = int(input("\nEnter a choice [1] Smallest Factor, [2] Prime Number or [0] Exit: "))

        if choice == 0:
            print("Program Terminated!")
            break
        elif choice == 1:
            smallestFactor()
        elif choice == 2:
            PrimeNumber()
        else:
            print("Invalid Choice! Please enter 1, 2 or 0 only.")

main()

