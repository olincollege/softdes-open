# Rubric for Assignment 6

## Submission

The submission should consist of three files:

- `tic_tac_toe_view.py`
- `tic_tac_toe_controller.py`
- `tic_tac_toe_game.py`

### Effort

For each file:

3: Changes to the file seem to show a good-faith attempt on all problem parts
relating to this file.

2: Changes to the file seem to show a good-faith attempt on at least 50% (but
strictly less than 100%) of problem parts relating to this file.

1: Changes to the file seem to show a good-faith attempt on less than 50% (but
strictly more than 0%) of problem parts relating to this file.

0: The file was unchanged from its initial state.

In this section, taking one or more late days results in full credit.

**Points: XX/6**

Grader comments: None.

### Scope of Changes

3: No files are added, changed, or deleted other than those listed above.

2: One file was added, changed, or deleted other than those listed above.

1: Two files were added, changed, or deleted other than those listed above.

0: Three or more files were added, changed, or deleted other than those listed
above.

**Points: XX/3**

Grader comments: None.

### Total

Add the point totals above.

**Points: XX/9**

## Correctness

The rubric describes some but not all possible point values and the criteria
that correspond to these values. Other point values are possible and given
subject to grader discretion.

### 1. An Inherited View (and an Acquired Taste)

The code for this problem is in `tic_tac_toe_view.py`.

#### 1.1. As Easy as `abc`

This part covers the classes `TicTacToeView` and `TextView` (implicitly) in
`tic_tac_toe_view.py`.

8: The implementation passes all unit tests.

5: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: XX/8**

Grader comments: None.

#### 1.2. A More Concrete View

This part covers the `draw` method of the `TextView` class in
`tic_tac_toe_view.py`.

8: The implementation passes all unit tests.

5: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: XX/8**

Grader comments: None.

#### An Inherited View (and an Acquired Taste) Summary

Add the points from the previous sections.

**Points: XX/16**

### 2. Taking Control

The code for this problem is in `tic_tac_toe_controller.py`.

#### Class Structure

This part covers the classes `TicTacToeController` and `TextController`
(implicitly) in `tic_tac_toe_controller.py`.

8: The implementation passes all unit tests.

5: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: XX/8**

Grader comments: None.

#### Move Input Processing

This part covers the `move` method of the `TextController` class in
`tic_tac_toe_controller.py`.

8: The implementation passes all unit tests.

5: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: XX/8**

Grader comments: None.

#### Taking Control Summary

Add the points from the previous sections.

**Points: XX/16**

### 3. All Together Now

The code for this problem is in `tic_tac_toe_game.py`, and concerns the `main`
function.

7: The implementation passes all unit tests.

4: The implementation fails some unit tests due to a minor error.

2: The implementation fails some unit tests due to a major error.

0: The implementation was not attempted or missing.

**Points: XX/7**

Grader comments: None.

### Correctness Summary

Add the points from the summary sections of each problem.

**Points: XX/39**

## Style

### General

2: The submission contains at most one spelling/grammar mistake.

1: The submission contains a few spelling/grammar mistakes.

0: The submission contains a substantial number of spelling/grammar mistakes.

**Points: XX/2**

Grader comments: None.

### Git

One point for meeting each of the following criteria (checked over all commits
relevant to the submission):

- The header line of commit message succinctly summarizes what was changed.
- The commit message provides context for the changes made.
- The commit does not add, edit, or remove files that are not necessary for
  submission (e.g., adding notes for yourself, or editing/removing the Jupyter
  notebook describing the assignment).
- The commit does not contain Git conflict indicators (e.g., `<<<<<<< HEAD`)
  that need to be removed during grading.
- The commit message does not contain lines that exceed 72 characters in length.

**Points: XX/5**

Grader comments: None.

### Black

For each of the 3 files submitted:

1: Black reports no formatting changes it would make to the file.

0: Black reports a formatting change it would make to the file.

**Points: XX/3**

Grader Comments: None.

### Pylint

Pylint, when run, returns a "style score" out of 10. After running this on all
Python files, take the style score and round it _down_, with minimum of 0
points.

**Points: XX/10**

Grader comments: None.

### Docstrings

This section covers docstrings for the functions listed below. For each
function:

2: The docstring is present, well-written, and includes all required
information.

1: The docstring has a minor error, such as not mentioning or explaining a
parameter/return type. (The parameter/return type is not required if there is
none, or if all information is easily and explicitly in the docstring summary.)

0: The docstring is missing or unchanged from the starter code.

In `tic_tac_toe_view.py`:

- `TicTacToeView`: **XX/2**
- `__init__`: **XX/2**
- `board`: **XX/2**
- `TicTacToeView.draw`: **XX/2**
- `TextView`: **XX/2**
- `TextView.draw`: **XX/2**

In `tic_tac_toe_controller.py`:

- `TicTacToeController`: **XX/2**
- `__init__`: **XX/2**
- `board`: **XX/2**
- `TicTacToeController.move`: **XX/2**
- `TextController`: **XX/2**
- `TextController.move`: **XX/2**

In `tic_tac_toe_game.py`:

- `main`: **XX/2**

**Points: XX/26**

Grader comments: None.

### Miscellaneous Code Style

Outside of where they are already covered by other parts of this rubric,
consider the following criteria (1 point each):

- Variable names follow the course guidelines for formatting and
  descriptiveness.
- The code consistently uses single or double quotes except where it would be
  convoluted to write.
- The code uses Python features taught in class (e.g., f-strings instead of
  `print` with multiple arguments, `str.format()`, or `%`-style strings).
- The code avoids "unpythonic" ways of writing things (e.g., `if x == True`
  instead of `if x`).
- Where needed, there are comments in the code to describe what a block of code
  does (at a high level) or why that code is there.
- The code is generally readable and easy to understand.

**Points: XX/6**

Grader comments: None.

### Overall Style Summary

Add up the points from all style subsection summaries.

**Points: XX/52**

## Summary

Copy the point totals from each of the four major section summaries above.

**Submission: XX/9**

**Correctness: XX/39**

**Style: XX/52**

### Total

**TOTAL POINTS: XX/100**

### Grader Information

_Grader_:

_Reviewer_:
