import pytest


@pytest.fixture(scope="module")
def preWork():
    print("MODULE => I setup browser instance by preWork")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("FUNCTION => I setup browser instance by secondWork")
    yield
    print("tear down validation")

@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print("This is first test.")
    assert preWork == "pass"

@pytest.mark.skip(reason="This is a skipped test.")
def test_secondCheck(preSetupWork, secondWork):
    print("This is second test.")
