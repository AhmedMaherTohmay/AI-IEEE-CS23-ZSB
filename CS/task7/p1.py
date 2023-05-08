import math


def main():
    """
    This is the main function of the program
    flips: numbre of filps of the coin
    ht: head or tail
    app: appearance of heads or tails
    prop: prropability of ht
    """
# checking the validity of the inputs
    while True:
        try:
            flips = int(input("Enter number of flips: "))
            break
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()

    while True:
        try:
            ht = str(input("Head or Tail? ")).lower()
            if ht not in ["head", "tail", "h", "t"]:
                print("invalid input")
                main()
            break
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()

    while True:
        try:
            app = int(input("The number of head appearance: "))
            break
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()

    while True:
        try:
            prop = float(input("The probability of tail (< 1): "))
            break
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()

    # for every probability we calculate it by multiplying every element
    # we can use power to make the multiplication as u can figure it out from the input
    # at last to u need to know how many times will u do the multiplication and this is done by combinations
    # multipling it with them will give u the answer
    ans = ((prop**app) * ((1 - prop)**(flips - app)))*math.comb(flips, app)
    print("the answer is: ")
    print(round(ans, 3))


if __name__ == "__main__":
    main()
