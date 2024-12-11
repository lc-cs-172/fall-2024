from search import search

def test_present():
    my_list = [1, 2, 3, 4, 5]
    assert search(my_list, 4) == 3

def test_absent():
    my_list = [1, 2, 3, 4, 5]
    assert search(my_list, 6) == -1

def test_empty():
    my_list = []
    assert search(my_list, 4) == -1
