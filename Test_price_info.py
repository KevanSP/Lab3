import price_info as pinf


def test_total_cost_shopping():
    result = pinf.total_cost_shopping()
    assert (result == 46.75)


def test_cost_of_fruit():
    result = pinf.cost_of_fruits('apple', 10)
    assert (result == 12.0)
