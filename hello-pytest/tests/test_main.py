import hello
import pytest


# testing the actions or "application"
@pytest.mark.smoke
def test_main(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result == "Hello, World!"
