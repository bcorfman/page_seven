from paging.format_pages import format_pages


def test_pages_2_out_of_5():
    assert format_pages(2, 5) == "1 (2) 3 4 5"


def test_pages_6_out_of_7():
    assert format_pages(6, 7) == "1 2 3 4 5 (6) 7"

