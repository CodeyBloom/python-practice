import hello


# The next few tests are for the "API"
def test_hello():
    result = hello.output()
    assert result == "Hello, World!"


def test_hello_comma():
    result = hello.output()
    assert "," in result


def test_hello_ends_with():
    result = hello.output()
    assert result.endswith("!")


# testing the parameters/args


def test_greeting():
    result = hello.output("-g Goodbye")
    assert result == "Goodbye, World!"


def test_long_greeting():
    result = hello.output("--greeting Goodbye")
    assert result == "Goodbye, World!"


def test_name():
    result = hello.output("-n Pytest")
    assert result == "Hello, Pytest!"


def test_long_name():
    result = hello.output("--name Pytest")
    assert result == "Hello, Pytest!"
