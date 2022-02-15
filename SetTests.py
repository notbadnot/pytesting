import pytest
#testsForSets
myset = {1, "hello", 15, 3.3}
myset.add(12)

def test_setFirst():
    assert 3.3 in myset


@pytest.mark.parametrize('inputValue, startSet', [("", {1,10,"bye"}), (1,  {1,10,"bye"}), (3, {1,10,"bye"}), ("hello", {1,10,"bye"}), ("bye", {1,10,"bye"})])
def test_setSecond(inputValue, startSet):
    initialLength = len(startSet)
    startSet.add(inputValue)
    finalLength = len(startSet)
    assert finalLength != initialLength

def test_setThird():
    try:
        assert myset.sort()
    except AttributeError:
        pass