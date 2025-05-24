import hello


# testing the actions or "application"
def test_main(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result == "Hello, World!"
