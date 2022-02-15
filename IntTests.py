import pytest
#tests for int
x = 15 

def test_firstInt():
    assert (x + 5) == 20


@pytest.mark.parametrize('inputedValue', [-3, -2.3, 0, 2.3, 3])
def test_second(inputedValue):
    assert ((inputedValue * x) % 5) == 0

def test_third():

    try:
        assert x + "av"
    except TypeError:
        pass
    

