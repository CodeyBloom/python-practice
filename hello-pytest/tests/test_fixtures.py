import pytest

# run this test suite and see the output to get a grok on fixtures. Notice how the setup and teardown
# are called before and after each test. Also notice how the setup is called once per module. This is
# really useful for setting up a test database or other resources that are needed for all tests but which
# are expensive to set up and tear down.


@pytest.fixture(scope="module")
def any_name():
    print("\nsetup")  # arrange / setup
    yield 5  # or return if no teardown needed
    print("teardown")  # cleanup / teardown


def test_a(any_name):
    print("do something")  # act
    print("assert something")  # assert
    assert any_name == 5


def test_b(any_name):
    print("do something")  # act
    print("assert something")  # assert
    assert any_name == 5
