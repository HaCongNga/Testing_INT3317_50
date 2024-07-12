def classify_student(mark, is_monitor=False, is_contributor=False):
    if not (0 <= mark <= 10):
        return "Invalid input"
    
    if is_monitor and is_contributor:
        if 9 <= mark <= 10:
            return "Good"
        elif 3 <= mark < 9:
            return "Passed"
        else:
            return "Failed"
    elif is_monitor or is_contributor:
        if 9 <= mark <= 10:
            return "Good"
        elif 4 <= mark < 9:
            return "Passed"
        else:
            return "Failed"
    else:
        if 9 <= mark <= 10:
            return "Good"
        elif 5 <= mark < 9:
            return "Passed"
        else:
            return "Failed"

# Functional test cases
boundary_test_cases = [
    (1, True, True, 0, "Failed"),
    (2, True, True, 0.1, "Failed"),
    (3, True, True, 5, "Passed"),
    (4, True, True, 9.9, "Good"),
    (5, True, True, 10, "Good"),
    (6, True, False, 0, "Failed"),
    (7, True, False, 0.1, "Failed"),
    (8, True, False, 5, "Passed"),
    (9, True, False, 9.9, "Good"),
    (10, True, False, 10, "Good"),
    (11, False, True, 0, "Failed"),
    (12, False, True, 0.1, "Failed"),
    (13, False, True, 5, "Passed"),
    (14, False, True, 9.9, "Good"),
    (15, False, True, 10, "Good"),
    (16, False, False, 0, "Failed"),
    (17, False, False, 0.1, "Failed"),
    (18, False, False, 5, "Passed"),
    (19, False, False, 9.9, "Good"),
    (20, False, False, 10, "Good"),
]

# Verify the function works correctly
for test_case in boundary_test_cases:
    test_id, is_monitor, is_contributor, mark, expected_output = test_case
    actual_output = classify_student(mark, is_monitor, is_contributor)
    status = "Pass" if actual_output == expected_output else "Fail"
    print(f"Test{test_id}_BoudaryTesting: ID={test_id}, Status={status}")