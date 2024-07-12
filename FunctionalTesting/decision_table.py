from boundary import classify_student

# Table test cases
table_test_cases = [
    (1, True, True, -1, "Invalid input"),
    (2, True, True, 2, "Failed"),
    (3, True, True, 3.5, "Passed"),
    (4, True, True, 4.5, "Passed"),
    (5, True, True, 6, "Passed"),
    (6, True, True, 9.5, "Good"),
    (7, True, True, 10.5, "Invalid input"),
    (8, True, False, -2, "Invalid input"),
    (9, True, False, 2.5, "Failed"),
    (10, True, False, 3.7, "Failed"),
    (11, True, False, 4.9, "Passed"),
    (12, True, False, 6.5, "Passed"),
    (13, True, False, 9.6, "Good"),
    (14, True, False, 10.9, "Invalid input"),
    (15, False, True, -1.5, "Invalid input"),
    (16, False, True, 2.4, "Failed"),
    (17, False, True, 3.4, "Failed"),
    (18, False, True, 4.4, "Passed"),
    (19, False, True, 6.9, "Passed"),
    (20, False, True, 9.2, "Good"),
    (21, False, True, 15, "Invalid input"),
    (22, False, False, -3, "Invalid input"),
    (23, False, False, 2.7, "Failed"),
    (24, False, False, 3.9, "Failed"),
    (25, False, False, 4.6, "Failed"),
    (26, False, False, 7.2, "Passed"),
    (27, False, False, 9.9, "Good"),
    (28, False, False, 20, "Invalid input"),
]

# Verify the function works correctly
for test_case in table_test_cases:
    test_id, is_monitor, is_contributor, mark, expected_output = test_case
    actual_output = classify_student(mark, is_monitor, is_contributor)
    status = "Pass" if actual_output == expected_output else "Fail"
    print(f"Test{test_id}_TableTesting: ID={test_id}, Status={status}")