def AdaptableSize(message):
    size = len(message) + 2

    print('~' * size)
    print(message.center(size))
    print('~' * size)


AdaptableSize("japanese food is awesome!")
AdaptableSize("food is coming")
AdaptableSize("name")
AdaptableSize("Programming in python is cool")