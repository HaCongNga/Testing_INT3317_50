from FunctionalTesting.boundary import classify_student

control_flow_test_cases = [
    (1, False, False, -5, "Invalid input"),
    (2, True, True, 9.5, "Good"),
    (3, True, True, 8, "Passed"),
    (4, True, True, 2, "Failed"),
    (5, True, False, 9.5, "Good"),
    (6, True, False, 8, "Passed"),
    (7, True, False, 2, "Failed"),
    (8, False, False, 9.2, "Good"),
    (9, False, False, 6.5, "Passed"),
    (10, False, False, 2, "Failed"),
]
# Verify the function works correctly
for test_case in control_flow_test_cases :
    test_id, is_monitor, is_contributor, mark, expected_output = test_case
    actual_output = classify_student(mark, is_monitor, is_contributor)
    status = "Pass" if actual_output == expected_output else "Fail"
    print(f"Test{test_id}_Control_flow: ID={test_id}, Status={status}")