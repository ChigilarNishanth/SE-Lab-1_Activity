"""
Course Registration System (Roll No: 56)
Handles student course registration, prerequisite validation, credit limits, and dropping courses.
"""

class CourseRegistrationSystem:
    def __init__(self, student_id: str, student_name: str, max_credits: int = 18):
        self.student_id = student_id
        self.student_name = student_name
        self.max_credits = max_credits
        self.completed_courses = set()
        self.enrolled_courses = {}
        self.total_registered_credits = 0

    def add_completed_course(self, course_code: str):
        self.completed_courses.add(course_code.upper())

    def register_course(self, course_code: str, course_name: str, credits: int, 
                        prerequisites: list = None, capacity: int = 30, current_enrolled: int = 0) -> str:
        course_code = course_code.upper()
        if prerequisites is None:
            prerequisites = []

        if credits <= 0:
            raise ValueError("Credits must be greater than zero.")

        if course_code in self.enrolled_courses:
            return "ALREADY_REGISTERED"

        if current_enrolled >= capacity:
            return "COURSE_FULL"

        for prereq in prerequisites:
            if prereq.upper() not in self.completed_courses:
                return f"MISSING_PREREQUISITE: {prereq}"

        if self.total_registered_credits + credits > self.max_credits:
            return "EXCEEDS_CREDIT_LIMIT"

        self.enrolled_courses[course_code] = {
            "name": course_name,
            "credits": credits
        }
        self.total_registered_credits += credits
        return "REGISTRATION_SUCCESS"

    def drop_course(self, course_code: str) -> bool:
        course_code = course_code.upper()
        if course_code not in self.enrolled_courses:
            return False

        dropped_info = self.enrolled_courses.pop(course_code)
        self.total_registered_credits -= dropped_info["credits"]
        return True

    def calculate_tuition_fee(self, cost_per_credit: float = 500.0) -> float:
        base_fee = self.total_registered_credits * cost_per_credit
        if self.total_registered_credits >= 12:
            return base_fee * 0.90
        return base_fee
