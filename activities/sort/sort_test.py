from sort import sort

def test_sort():
    my_list = [13, 7, 3, 15, 9, 17, 18, 19, 20, 16, 11, 4, 12, 5, 8, 10]
    sorted =  [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    sort(my_list)
    assert my_list == sorted
