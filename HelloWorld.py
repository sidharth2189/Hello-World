# A unction where the string
# "Hello World!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# and the string is returned with "return".
# The string is only used once in the code.


def show_excitement():
    # Your code goes here!
    list = []
    string = "Hello World!"
    for index in range(5):
        list.append(string)
    return(' '.join(map(str, list)))

print show_excitement()
