from FunctionalTesting.boundary import classify_student

data_flow_test_cases = [
    (1, False, False, 12, "Invalid input"),
    (2, True, True, 10, "Good"),
    (3, True, True, 3, "Passed"),
    (4, True, True, 2, "Failed"),
    (5, True, False, 10, "Good"),
    (6, True, False, 4, "Passed"),
    (7, True, False, 3, "Failed"),
    (8, False, False, 10, "Good"),
    (9, False, False, 5, "Passed"),
    (10, False, False, 4, "Failed"),
]
# Verify the function works correctly
for test_case in data_flow_test_cases :
    test_id, is_monitor, is_contributor, mark, expected_output = test_case
    actual_output = classify_student(mark, is_monitor, is_contributor)
    status = "Pass" if actual_output == expected_output else "Fail"
    print(f"Test{test_id}_data_flow: ID={test_id}, Status={status}")