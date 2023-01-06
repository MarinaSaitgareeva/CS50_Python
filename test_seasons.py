from seasons import check_date
import pytest


def main():
    test_missing_date()
    test_incorrect_date_format()
    test_incorrect_date()
    test_correct_date()


def test_missing_date():
    with pytest.raises(SystemExit) as my_sys_exit_error:
        check_date("")
    assert my_sys_exit_error.type == SystemExit
    assert my_sys_exit_error.value.code == "Missing date"


def test_incorrect_date_format():
    with pytest.raises(SystemExit) as my_sys_exit_error:
        check_date("Jan 1, 1988")
    assert my_sys_exit_error.type == SystemExit
    assert my_sys_exit_error.value.code == "Invalid date"


def test_incorrect_date():
    with pytest.raises(SystemExit) as my_sys_exit_error:
        check_date("70-70-70")
    assert my_sys_exit_error.type == SystemExit
    assert my_sys_exit_error.value.code == "Invalid date"


def test_correct_date():
    assert check_date("1988-01-01") == (1988, 1, 1)


if __name__ == "__main__":
    main()
