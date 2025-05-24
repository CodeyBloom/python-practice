import hello


# testing the actions or "application"
def test_main(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result == "Hello, World!"


# and the next few test the "API"
def test_hello():
    result = hello.output()
    assert result == "Hello, World!"


def test_hello_comma():
    result = hello.output()
    assert "," in result


def test_hello_ends_with():
    result = hello.output()
    assert result.endswith("!")
