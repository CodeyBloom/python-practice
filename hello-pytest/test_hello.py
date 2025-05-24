import hello

def test_hello(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result == "Hello, World!"

def test_hello_comma(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert ',' in result

def test_hello_ends_with(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result.endswith('!')
