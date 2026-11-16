from typing import Any


def assert_status_code(actual:int,expected:int):
    assert actual==expected, (
        f'Incorrect status code'
        f'Expected {expected} '
        f'Actual {actual} '
    )


def assert_equal(actual:Any,expected:Any,name:str):
    assert actual==expected, (
        f'Incorrect value {name} '
        f'Expected {expected} '
        f'Actual {actual} '
    )