#Creating a cool conditional statement

name = input("Enter your name: ")

ascii_name = ''
MAXIMUM_LENGTH = 6


if (len(name) > MAXIMUM_LENGTH):
    print("Wow why such a long name?")

else:
    print("That is the right amount of letters for any name!")

for char in name:
    ascii_name += str(ord(char))


print("Well either way whether your name is long or short" +
        "here is your name in ascii characters {}".format(ascii_name))





