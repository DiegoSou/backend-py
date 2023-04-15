# pylint: disable=W1514


def start():
    """Start function
    :params -
    :return - print test
    """
    print("test")


with open("file.txt", "r") as arquivo:
    print(arquivo.readline())
