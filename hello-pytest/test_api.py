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
