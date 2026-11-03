# Lab 6: Code and Branch Coverage Analysis

**Student Roll No:** 56  
**Application:** Course Registration System (`course_registration.py`)  

---

## 1. Executive Summary

This lab demonstrates the difference between **Line (Code) Coverage** and **Branch Coverage** using Python's `coverage` library and `pytest` framework.

- **Code Coverage Achieved:** 100%
- **Branch Coverage Achieved:** 100%

---

## 2. Line Coverage Analysis

Line coverage measures whether every executable line of code was executed during testing[cite: 1].

### Execution Command
```bash
coverage run -m pytest CodeCoverageTest_56_course_registration.py
coverage report -m
Report ResultsMetricResultTotal Statements40Covered Statements40Line Coverage100%AnalysisAll 40 executable statements were covered by the automated test cases. Every line in course_registration.py was executed during line coverage testing.
```
---

## 3. Branch Coverage Analysis
Branch coverage evaluates whether every decision point in the application was tested for both True and False outcomes.   Decision Branches CoveredCredit Validation (credits <= 0)Valid credit values.Invalid zero or negative credits resulting in a ValueError exception.Duplicate Course Registration (course_code in self.enrolled_courses)Registering a new course.Attempting to register an already enrolled course (ALREADY_REGISTERED).Course Capacity (current_enrolled >= capacity)Registering when seats are available.Attempting registration when full (COURSE_FULL).Prerequisite Validation (prereq.upper() not in self.completed_courses)Registering when prerequisites are satisfied.Attempting registration with missing prerequisites (MISSING_PREREQUISITE).Maximum Credit Limit (self.total_registered_credits + credits > self.max_credits)Registering within credit limit.Exceeding maximum credit limit (EXCEEDS_CREDIT_LIMIT).Course Drop Validation (course_code not in self.enrolled_courses)Successfully dropping an enrolled course (True).Attempting to drop a non-enrolled course (False).Tuition Fee Calculation (self.total_registered_credits >= 12)Standard tuition fee (< 12 credits).10% overload discount (>= 12 credits).Execution CommandsBashcoverage run --branch -m pytest BranchCoverageTest_56_course_registration.py
coverage report -m
Report ResultsMetricResultTotal Statements40Total Branches18Branch Coverage100%AnalysisBranch coverage provides a deeper assessment than line coverage alone[cite: 3]. It verifies that all conditional decisions (both True and False branches) have been exercised.   

---

## 4. Key TakeawaysLine vs. Branch Coverage: 
Achieving 100% line coverage does not guarantee 100% branch coverage[cite: 3]. Branch coverage ensures edge cases in control flow are fully tested.   Edge Cases Tested: Zero/negative credits, capacity limits, duplicate registrations, missing prerequisites, overload credit limits, invalid drops, and fee discount thresholds[cite: 1]. 

---

## 5. Rubric Verification Checklist
Rubric CriteriaRequired ItemsStatusCode Coverage Analysis & Report (2 Marks)Terminal Screenshot and README.md sectionComplete   Branch Coverage Analysis & Report (2 Marks)Terminal Screenshot and README.md sectionComplete   Commits and Testcases (>90%) (6 Marks)Test case files (CodeCoverageTest_56_course_registration.py, BranchCoverageTest_56_course_registration.py), test execution, and Git commits pushed to main branchComplete   Test FilesCodeCoverageTest_56_course_registration.pyBranchCoverageTest_56_course_registration.py

---
