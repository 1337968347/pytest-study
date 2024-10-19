import pytest

def func(x):
    return x+1

def test_answer():
    assert func(1) == 2

def f():
    raise ExceptionGroup(
        "error messages",
        RuntimeError(),
        TypeError())

def test_mytest():
    with pytest.raises(ExceptionGroup) as epinfo:
        f()
    assert epinfo.group_contains(RuntimeError)
    assert epinfo.group_contains(ZeroDivisionError)