import Lab2_2320.bmi as BMI
# can also use: from Lab2_2320 import bmi as BMI


def test_bmi_normal_weight():
    height=1.65
    weight=67.0
    answer = 0
    result = BMI.calculate_bmi(height, weight)
    assert(result==answer)



def test_bmi_over_weight():
    height=1.65
    weight=97.0
    answer = 1
    result = BMI.calculate_bmi(height, weight)
    assert(result==answer)



def test_bmi_under_weight():
    height=1.65
    weight=47.0
    answer = -1
    result = BMI.calculate_bmi(height, weight)
    assert(result==answer)