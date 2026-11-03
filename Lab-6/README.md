# Lab 6: Code and Branch Coverage Analysis

**Student:** Nishanth T Chigilar  
**Roll No.:** 56  
**Application:** Course Registration System (`course_registration.py`)

## 1. Objective

This lab demonstrates the difference between **line (code) coverage** and **branch coverage** using `pytest` and the Python `coverage` package.

- **Line coverage:** verifies that executable statements are run.
- **Branch coverage:** verifies that both outcomes of conditional decisions are tested.

## 2. Project Files

| File | Description |
| --- | --- |
| `course_registration.py` | Course registration system implementation |
| `CodeCoverageTest_56_course_registration.py` | Functional tests used for line coverage |
| `BranchCoverageTest_56_course_registration.py` | Tests designed to exercise both branch outcomes |

## 3. Line Coverage Analysis

Line coverage tests the following functionality:

- Successful course registration
- Completed-course management
- Duplicate-registration handling
- Course-capacity validation
- Prerequisite validation
- Maximum-credit validation
- Invalid-credit error handling
- Course dropping
- Tuition-fee calculation

### Run the line coverage tests

```bash
coverage run -m pytest CodeCoverageTest_56_course_registration.py
coverage report -m
```

### Result

The test suite covers all executable statements in `course_registration.py`, resulting in **100% line coverage**.

## 4. Branch Coverage Analysis

The branch tests cover both outcomes of these decisions:

| Decision | True outcome | False outcome |
| --- | --- | --- |
| `credits <= 0` | Raises `ValueError` | Registration continues |
| Course already enrolled | Returns `ALREADY_REGISTERED` | Registration continues |
| Course is full | Returns `COURSE_FULL` | Registration continues |
| Prerequisite is missing | Returns `MISSING_PREREQUISITE` | Registration continues |
| Credit limit exceeded | Returns `EXCEEDS_CREDIT_LIMIT` | Registration succeeds |
| Course exists when dropping | Removes the course | Returns `False` |
| Credits are at least 12 | Applies the 10% tuition discount | Charges the standard fee |

### Run the branch coverage tests

```bash
coverage run --branch -m pytest BranchCoverageTest_56_course_registration.py
coverage report -m
```

### Result

The branch test suite exercises both outcomes of each conditional decision, resulting in **100% branch coverage**.

## 5. Key Takeaways

- Line coverage confirms that executable statements have been run.
- Line coverage alone does not guarantee that every decision outcome has been tested.
- Branch coverage provides stronger confidence by testing both sides of each condition.
- The tests include edge cases such as invalid credits, full courses, duplicate registrations, missing prerequisites, credit-limit violations, invalid drops, and tuition-discount thresholds.

## 6. Rubric Checklist

| Requirement | Evidence | Status |
| --- | --- | --- |
| Code coverage analysis and report | This README and `CodeCoverageTest_56_course_registration.py` | Complete |
| Branch coverage analysis and report | This README and `BranchCoverageTest_56_course_registration.py` | Complete |
| Test coverage above 90% | Coverage commands and test files | Complete |
| Code and test files committed | `Lab-6/` contents in the repository | Complete |

