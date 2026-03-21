import pytest


def test_thirdCheck(preSetupWork):
    print("This is third test.")

@pytest.mark.smoke
def test_fourthCheck(preSetupWork):
    print("This is fourth test.")
