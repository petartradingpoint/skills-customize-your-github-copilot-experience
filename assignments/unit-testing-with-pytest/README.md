# 📘 Assignment: Unit Testing with pytest

## 🎯 Objective

Learn the fundamentals of automated testing by writing unit tests with pytest. You'll develop test cases for a simple calculator module, understand the red-green-refactor cycle, and gain confidence in verifying code behavior through comprehensive test coverage.

## 📝 Tasks

### 🛠️ Write Tests for Calculator Functions

#### Description
You are given a starter module with basic calculator functions. Your task is to write comprehensive unit tests using pytest that verify each function works correctly with typical inputs, edge cases, and error conditions. Tests should be clear, focused, and follow pytest conventions.

#### Requirements
Completed program should:

- Write at least 3 tests for the `add()` function, covering normal cases and edge cases (e.g., zero, negatives, large numbers)
- Write at least 3 tests for the `subtract()` function with similar coverage
- Write at least 3 tests for the `multiply()` function, including zero and negative cases
- Write at least 2 tests for the `divide()` function, including division by zero (expect an exception)
- Run all tests using `pytest` and confirm they all pass
- Organize tests into a single test file using clear function names that describe what is being tested

### 🛠️ Red-Green-Refactor Exercise

#### Description
Implement a new function `power(base, exponent)` that raises a base to an exponent. Follow the Test-Driven Development (TDD) approach: write the test first (red), implement the function to pass the test (green), then refactor if needed.

#### Requirements
Completed program should:

- Write at least 2 test cases for the `power()` function before implementing it
- Run tests and confirm they fail (red phase)
- Implement the `power()` function to make the tests pass (green phase)
- Verify all tests pass, including the new ones
- Document the TDD process in a comment explaining your approach (optional but encouraged)

### 🛠️ Test Edge Cases and Error Handling

#### Description
Extend your test suite to handle edge cases and error conditions. Consider boundary values, special cases, and invalid inputs. Write tests that expect exceptions when appropriate.

#### Requirements
Completed program should:

- Add tests for at least one edge case (e.g., dividing by zero should raise `ZeroDivisionError`)
- Add tests for at least one boundary value (e.g., very large or very small numbers)
- Use `pytest.raises()` to verify that exceptions are raised correctly
- Verify that invalid inputs are handled as expected (or raise appropriate exceptions)
- Achieve at least 90% code coverage for all functions in the calculator module
