"""For best practices with pytest I can separate my actions from computations, so I only need to call "capsys" one one
test (the one testing the actions) not all of them. See the tests to grok it"""

# this is like a little mock API for hello world, all evalutation
import argparse


def parse_args(arg_str: str | None = ""):
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--greeting", type=str, default="Hello")
    parser.add_argument("-n", "--name", type=str, default="World")

    arg_list = None if arg_str is None else arg_str.split()

    args = parser.parse_args(arg_list)

    return args


def output(arg_str: str | None = ""):
    args = parse_args(arg_str)
    return f"{args.greeting}, {args.name}!"


# then this is like a little application that uses the API, with actions
def main(arg_str: str | None = ""):
    print(output(arg_str))


if __name__ == "__main__":
    main()
