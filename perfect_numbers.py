## write a Python program that asks the user for an integer number and
## then prints out whether the number is a perfect number or not.
import sys


def is_perfect_number(n):
    if n < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n


def main():
    if len(sys.argv) != 2:
        print("Usage: python perfect_numbers.py <integer>")
        return

    try:
        number = int(sys.argv[1])
        if is_perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
    except ValueError:
        print("Please provide a valid integer.")


if __name__ == "__main__":
    main()
