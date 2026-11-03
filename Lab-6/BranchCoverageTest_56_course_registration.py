import pytest
from course_registration import CourseRegistrationSystem

class TestBranchCoverage:

    def test_invalid_credits_branch(self):
        system = CourseRegistrationSystem("56", "Nishanth")
        with pytest.raises(ValueError):
            system.register_course("CS101", "Intro", 0)

    def test_already_registered_branch(self):
        system = CourseRegistrationSystem("56", "Nishanth")
        res1 = system.register_course("CS101", "Intro", 3)
        assert res1 == "REGISTRATION_SUCCESS"
        res2 = system.register_course("CS101", "Intro", 3)
        assert res2 == "ALREADY_REGISTERED"

    def test_course_full_branch(self):
        system = CourseRegistrationSystem("56", "Nishanth")
        res_full = system.register_course("CS102", "Web Dev", 3, capacity=10, current_enrolled=10)
        assert res_full == "COURSE_FULL"
        res_ok = system.register_course("CS103", "Web Dev", 3, capacity=10, current_enrolled=5)
        assert res_ok == "REGISTRATION_SUCCESS"

    def test_prerequisite_branch(self):
        system = CourseRegistrationSystem("56", "Nishanth")
        system.add_completed_course("CS101")
        res_prereq_ok = system.register_course("CS102", "Advanced CS", 3, prerequisites=["CS101"])
        assert res_prereq_ok == "REGISTRATION_SUCCESS"
        res_prereq_missing = system.register_course("CS301", "AI", 3, prerequisites=["CS201"])
        assert res_prereq_missing == "MISSING_PREREQUISITE: CS201"

    def test_credit_limit_branch(self):
        system = CourseRegistrationSystem("56", "Nishanth", max_credits=10)
        res_exceed = system.register_course("CS202", "OS", 12)
        assert res_exceed == "EXCEEDS_CREDIT_LIMIT"

    def test_drop_course_branches(self):
        system = CourseRegistrationSystem("56", "Nishanth")
        system.register_course("CS101", "Intro", 3)
        assert system.drop_course("CS101") is True
        assert system.drop_course("CS101") is False

    def test_tuition_fee_branches(self):
        system = CourseRegistrationSystem("56", "Nishanth")
        system.register_course("CS101", "Intro", 5)
        assert system.calculate_tuition_fee(100.0) == 500.0
        system.register_course("CS102", "Core", 7)
        assert system.calculate_tuition_fee(100.0) == 1200.0 * 0.90
