import pytest
from course_registration import CourseRegistrationSystem

def test_successful_registration():
    system = CourseRegistrationSystem("56", "Nishanth", max_credits=18)
    res = system.register_course("CS101", "Python Programming", 4)
    assert res == "REGISTRATION_SUCCESS"
    assert system.total_registered_credits == 4

def test_add_completed_course():
    system = CourseRegistrationSystem("56", "Nishanth")
    system.add_completed_course("CS101")
    assert "CS101" in system.completed_courses

def test_already_registered():
    system = CourseRegistrationSystem("56", "Nishanth")
    system.register_course("CS101", "Python", 4)
    res = system.register_course("CS101", "Python", 4)
    assert res == "ALREADY_REGISTERED"

def test_course_full():
    system = CourseRegistrationSystem("56", "Nishanth")
    res = system.register_course("CS102", "Data Structures", 4, capacity=30, current_enrolled=30)
    assert res == "COURSE_FULL"

def test_missing_prerequisite():
    system = CourseRegistrationSystem("56", "Nishanth")
    res = system.register_course("CS201", "Algorithms", 4, prerequisites=["CS101"])
    assert res == "MISSING_PREREQUISITE: CS101"

def test_exceeds_credit_limit():
    system = CourseRegistrationSystem("56", "Nishanth", max_credits=6)
    res = system.register_course("CS301", "Database Systems", 8)
    assert res == "EXCEEDS_CREDIT_LIMIT"

def test_invalid_credits_exception():
    system = CourseRegistrationSystem("56", "Nishanth")
    with pytest.raises(ValueError, match="Credits must be greater than zero."):
        system.register_course("CS100", "Zero Credit Course", 0)

def test_drop_course_success():
    system = CourseRegistrationSystem("56", "Nishanth")
    system.register_course("CS101", "Python", 4)
    assert system.drop_course("CS101") is True
    assert system.total_registered_credits == 0

def test_drop_course_not_found():
    system = CourseRegistrationSystem("56", "Nishanth")
    assert system.drop_course("CS999") is False

def test_calculate_tuition_fee():
    system = CourseRegistrationSystem("56", "Nishanth")
    system.register_course("CS101", "Python", 4)
    system.register_course("CS102", "Maths", 8)
    fee = system.calculate_tuition_fee(cost_per_credit=500.0)
    assert fee == (12 * 500.0) * 0.90
