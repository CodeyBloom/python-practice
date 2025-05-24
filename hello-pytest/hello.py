"""For best practices with pytest I can separate my actions from computations, so I only need to call "capsys" one one
test (the one testing the actions) not all of them. See the tests to grok it"""


# this is like a little mock API for hello world, all pure evalutation
def output():
    return "Hello, World!"


# then this is like a little application that uses the API, with actions
def main():
    print(output())


if __name__ == "__main__":
    main()
