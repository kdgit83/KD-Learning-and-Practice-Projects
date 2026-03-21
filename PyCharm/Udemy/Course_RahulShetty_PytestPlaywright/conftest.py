import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("SESSION => I setup browser instance")