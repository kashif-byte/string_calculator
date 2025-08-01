## String Calculator TDD Kata

A Test-Driven Development implementation of the String Calculator kata for Incubyte assessment.



This project demonstrates Test-Driven Development (TDD) principles by implementing a string calculator that can:
- Handle empty strings and single numbers
- Sum comma-separated numbers
- Support newline delimiters
- Handle custom delimiters
- Validate against negative numbers

## Tech Stack

-   Language: Python 3.x
-   Testing Framework: pytest
-   Development Approach: Test-Driven Development (TDD)

## Requirements

- Python 3.7+
- pytest

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kashif-byte/string_calculator.git
   cd string_calculator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=string_calculator

# Run specific test file
pytest test_string_calculator.py -v
```

## 📊 Test Results

### Current Test Coverage


### All Tests Passing
[Screenshot of all tests passing]

![All Tests Passing](screenshots/all_tests_passing.png)

## 🔄 TDD Process

This project follows the Red-Green-Refactor cycle:

1. **🔴 Red**: Write a failing test
2. **🟢 Green**: Write minimal code to make it pass
3. **🔵 Refactor**: Improve the code while keeping tests green

### Git Commit History
Each commit represents a step in the TDD process:

![Commit History](screenshots/commit_history.png)

## 📝 Implementation Details

### Features Implemented

- ✅ **Empty String**: Returns 0
- ✅ **Single Number**: Returns the number itself
- ✅ **Two Numbers**: Returns sum of both numbers
- ✅ **Multiple Numbers**: Handles any amount of numbers
- ✅ **Newline Support**: Supports `\n` as delimiter
- ✅ **Custom Delimiters**: Supports format `//[delimiter]\n[numbers]`
- ✅ **Negative Number Validation**: Throws exception with all negative numbers

### Usage Examples

```python
from string_calculator import add

# Basic usage
add("")           # Returns: 0
add("1")          # Returns: 1
add("1,5")        # Returns: 6
add("1,2,3,4,5")  # Returns: 15

# Newline support
add("1\n2,3")     # Returns: 6


# Negative numbers (throws exception)
add("-1,2")       # Raises: NegativeNumberError
```


string_calculator/
├── string_calculator.py      # Main implementation
├── test_string_calculator.py # Test suite
├── exceptions.py             # Custom exceptions
├── requirements.txt          # Dependencies
├── README.md                # Documentation
├── .gitignore               # Git ignore rules
└── screenshots/             # Screenshots for documentation
    ├── test_coverage.png
    ├── all_tests_passing.png
    └── commit_history.png
```

##Screenshots

### Test Execution
![Test Execution](screenshots/test_execution.png)

### TDD Red-Green-Refactor Cycle
![TDD Cycle](screenshots/tdd_cycle.png)

## TDD Best Practices Demonstrated

- **Incremental Development**: Each feature built step by step
- **Frequent Commits**: Every Red-Green-Refactor cycle committed
- **Clean Code**: Readable and maintainable implementation
- **Comprehensive Testing**: Edge cases and error conditions covered
- **Refactoring**: Code improved while maintaining functionality


