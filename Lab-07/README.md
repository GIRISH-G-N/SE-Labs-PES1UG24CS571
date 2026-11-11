# Lab 07 – Fuzzing for Input Validation Bugs

<p align="center">
  <b>Software Engineering Laboratory</b><br>
  Hotel Booking Application
</p>

---

## Student Information

| Field | Details |
|---|---|
| **Name** | Girish G N |
| **SRN** | PES1UG24CS571 |
| **Course** | Software Engineering |
| **Lab** | 07 – Fuzzing for Input Validation Bugs |

## Project Overview

This laboratory exercise focuses on identifying and fixing input-validation bugs using **Fuzz Testing** and **Property-Based Testing**.

The Hotel Booking application contains three functions that process user inputs. Hypothesis is used to generate different types of inputs, including malformed strings, empty values and `None`, to identify unexpected crashes.

The application is then improved with appropriate input validation and safe error handling.

## Objectives

- Understand the concept of fuzz testing and property-based testing.
- Identify input-validation vulnerabilities in Python functions.
- Generate test inputs automatically using Hypothesis.
- Detect application crashes and unexpected exceptions.
- Implement input validation and defensive programming.
- Verify the corrected application using automated tests.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Application development |
| Hypothesis | Property-based and fuzz testing |
| Pytest | Automated test execution |
| Windows CMD | Execution and testing environment |
| Git & GitHub | Version control and submission |

## Application Functions

The Hotel Booking application contains the following three functions:

### 1. `nights_stayed(days)`

Calculates the number of nights between check-in and check-out days.

**Example:**
```python
nights_stayed("12-15")
```
**Output:** `3`

### 2. `room_floor(room_code)`

Extracts the floor number from a hotel room code.

**Example:**
```python
room_floor("D-305")
```
**Output:** `3`

### 3. `booking_label(names_csv)`

Generates a booking label using the lead guest's name and the number of additional guests.

**Example:**
```python
booking_label("ravi, priya")
```
**Output:** `Ravi +1`

## Fuzz Testing Methodology

Hypothesis was used to generate a wide variety of inputs automatically.

The test cases use:

- Random text inputs.
- Empty strings.
- Special characters.
- Missing or malformed values.
- `None` values.

Each function is tested to verify that unexpected inputs do not cause an unhandled exception.

### Initial Testing

The original application contained input-handling problems.

Hypothesis identified failures in all three functions:

| Function | Identified Problems |
|---|---|
| `nights_stayed()` | Invalid date format, missing values and `None` |
| `room_floor()` | Missing room number, invalid characters and `None` |
| `booking_label()` | Empty guest list and `None` |

**Initial test result: 3 failed**

### Bug Fixes and Improvements

The application was updated with defensive input validation.

- **`nights_stayed()`** – Validates input type, date format, empty components and day order.
- **`room_floor()`** – Validates room-code structure and numeric room information.
- **`booking_label()`** – Handles non-string and empty inputs, filters blank guest names and provides a fallback label.

## Final Testing Results

After implementing the fixes, the same Hypothesis tests were executed again using Pytest.

**Final result: 3 passed**

| Test Case | Result |
|---|---|
| `test_nights_stayed_no_crash` | PASSED |
| `test_room_floor_no_crash` | PASSED |
| `test_booking_label_no_crash` | PASSED |

All three functions successfully completed the generated no-crash tests.

## Project Structure

```text
Lab-07/
│
├── hotel_booking.py
├── test_hotel_booking.py
│
├── SS -01.png
├── SS-03.png
├── 04_fixed_output.png
├── 05_passing_tests.png
│
├── Lab_7_Fuzzing_Input_Validation_Report_Girish_G_N.pdf
│
└── README.md
```

## Execution Instructions

### 1. Install Dependencies

```bash
pip install hypothesis pytest
```

### 2. Run the Application

```bash
python hotel_booking.py
```

### 3. Execute Fuzz Tests

```bash
python -m pytest test_hotel_booking.py -v
```

### Expected Test Summary

```text
test_nights_stayed_no_crash PASSED
test_room_floor_no_crash PASSED
test_booking_label_no_crash PASSED

3 passed
```

## Screenshots and Documentation

The following screenshots document the testing process:

| Screenshot | Description |
|---|---|
| `SS -01.png` | Environment setup and original application failure |
| `SS-03.png` | Initial Hypothesis test failures |
| `04_fixed_output.png` | Corrected application execution |
| `05_passing_tests.png` | Final successful test execution |

**Detailed Laboratory Report:**

[Download Lab 07 PDF Report](Lab_7_Fuzzing_Input_Validation_Report_Girish_G_N.pdf)

## Related Repository

The complete Hotel Booking application work for Lab 06 and Lab 07 is maintained in my forked repository.

<p align="center">
  <a href="https://github.com/GIRISH-G-N/L6_L7_22_hotel_booking">
    <b>VIEW FORKED REPOSITORY – L6_L7_22_hotel_booking</b>
  </a>
</p>

This repository includes the application implementation, coverage analysis, fuzz testing, source code, screenshots and documentation.

---

## Conclusion

This laboratory exercise demonstrates how fuzz testing and property-based testing can identify input-validation bugs that may not be detected through ordinary test cases.

By using Hypothesis and Pytest, unexpected input conditions were identified, the application was improved with defensive validation, and all three no-crash tests passed.

---

**Submitted by:** Girish G N  
**SRN:** PES1UG24CS571
