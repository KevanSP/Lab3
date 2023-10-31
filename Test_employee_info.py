import employee_info as einfo


def test_get_employees_by_age_range():
    AgeUpper = 35
    AgeLower = 25
    true_arr = [{'age': 30, 'department': 'Sales', 'name': 'John', 'salary': 50000},
                {'age': 32, 'department': 'Engineering', 'name': 'Mike', 'salary': 65000}]

    result = einfo.get_employees_by_age_range(AgeLower, AgeUpper)
    assert (result == true_arr)


def test_calculate_average_salary():
    result = einfo.calculate_average_salary()
    assert (round(result) == 60167)


def test_get_employees_by_dept():
    dept = "Engineering"
    true_arr = [{'age': 35, 'department': 'Engineering', 'name': 'Chloe', 'salary': 70000},
                {'age': 32, 'department': 'Engineering', 'name': 'Mike', 'salary': 65000}]

    result = einfo.get_employees_by_dept(dept)
    assert (result == true_arr)
