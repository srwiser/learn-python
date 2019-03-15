## Print digits of a number in a pattern

def printPattern(number):
    count = 0
    while number > 0:
        number = number / 10
        count += 1
    digits = count
    for i in range(digits):
        n1 = divmod(number,10^(digits-i))
        print(n1)

if __name__ == "__main__":
    str = input("Enter Number: ")
    number = int(str)
    printPattern(number)