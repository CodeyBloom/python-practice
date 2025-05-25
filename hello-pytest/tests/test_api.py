import hello
import pytest


# The next few tests are for the "API"
def test_hello():
    result = hello.output()
    assert result == "Hello, World!"


@pytest.mark.smoke
def test_hello_comma():
    result = hello.output()
    assert "," in result


def test_hello_ends_with():
    result = hello.output()
    assert result.endswith("!")


# testing the parameters/args


# this one combines all the following int a single test, its very useful
@pytest.mark.parametrize(
    "arg_str, expected",
    [
        ("-g Goodbye", "Goodbye, World!"),
        ("--greeting Goodbye", "Goodbye, World!"),
        ("-n Pytest", "Hello, Pytest!"),
        ("--name Pytest", "Hello, Pytest!"),
        pytest.param(
            "-g Goodbye -n Pytest", "Goodbye, Pytest!", marks=pytest.mark.smoke
        ),
    ],
    ids=lambda x: f'"{x}"',
)
def test_output(arg_str, expected):
    result = hello.output(arg_str)
    assert result == expected


@pytest.mark.parametrize("arg_str", ["-n Pytest", "--name Pytest"])
def test_name(arg_str):
    result = hello.output(arg_str)
    assert result == "Hello, Pytest!"


def test_long_name():
    result = hello.output("--name Pytest")
    assert result == "Hello, Pytest!"
