

# checks input is a number more than zero
def num_check(question):


    valid = False
    while not valid:

        error1 = "please enter a number that is more than zero"
        error2 = "please enter a number"
        try:

            response = float(input(question))

            if response > 0:
                return response 

            else:
                print(error1)
                print()

        except ValueError:
            print(error2)
            print()

print()
print("***** Area / Perimeter Calculator *****")
print()

looping = ""
while looping == "":

    width = num_check("width: ")
    height = num_check("height: ")

    area = width*height
    perimeter = 2*(width + height)

    print("Perimeter: {:.2f} units".format(perimeter))
    print("Area: {:.2f} square units".format(area))
    print()


    looping = input("press <enter> to continue or any key to quit")

print()
print("thank you for using the area / perimeter calculator")    