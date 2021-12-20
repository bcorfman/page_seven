from paging.display import Pages


def test_display_2_selected_out_of_5():
    pages = Pages(selected=2, total=5)
    assert pages.display() == '1 (2) 3 4 5'


def test_display_6_selected_out_of_7():
    pages = Pages(selected=6, total=7)
    assert pages.display() == '1 2 3 4 5 (6) 7'
