import pytest

@pytest.mark.xfail(reason="Known issue")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Known issue2")
def test_without_bug():
    pass