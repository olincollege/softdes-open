# Rubric for Assignment 5

## Submission

The submission should consist of two files:

- `tic_tac_toe.py`
- `user_account.py`

### Timeliness

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

In all cells requiring a solution, a missing solution is automatically given 0
points.

The rubric describes some but not all possible point values and the criteria
that correspond to these values. Other point values are possible and given
subject to grader discretion.

### 1. A Cure for Your Board-om

The code for this problem is in `tic_tac_toe.py`.

For each of the six methods to implement (`__init__`, `next_move`, `mark`,
`get_square`, `check_win`, and `__repr__`):

4: The method passes all unit tests.

3: The method fails some unit tests due to a minor error.

2: The method fails some unit tests due to a major error.

0: The method was not attempted or missing.

- `__init__`: **XX/4**
- `next_move`: **XX/4**
- `mark`: **XX/4**
- `get_square`: **XX/4**
- `check_win`: **XX/4**
- `__repr__`: **XX/4**

**Points: XX/24**

Grader comments: None.

### 2. _Ex Post Refacto_

The code for this problem is in `user_account.py`.

#### 2.1. `@property` Value

This step concerns any method in `UserAccount` that references the variables
originally named `username` or `posts`.

6: The refactored implementation passes all unit tests.

4: The refactored implementation fails some unit tests due to a minor error.

2: The refactored implementation fails some unit tests due to a major error.

0: The refactored implementation was not attempted or missing.

**Points: XX/6**

Grader comments: None.

#### 2.2. A-`dict`-ed to Refactoring

This step concerns any method in `UserAccount` that references the variable
originally named `posts`, as well as the new method `num_posts`.

6: The refactored implementation passes all unit tests.

4: The refactored implementation fails some unit tests due to a minor error.

2: The refactored implementation fails some unit tests due to a major error.

0: The refactored implementation was not attempted or missing.

**Points: XX/6**

Grader comments: None.

#### 2.3. Moving the Post Goals

This step concerns the `post` method in `UserAccount` and the
`generate_new_post_id` function outside of `UserAccount`.

6: The refactored implementation passes all unit tests.

4: The refactored implementation fails some unit tests due to a minor error.

2: The refactored implementation fails some unit tests due to a major error.

0: The refactored implementation was not attempted or missing.

**Points: XX/6**

Grader comments: None.

#### _Ex Post Refacto_ Summary

Add the points from the previous sections.

**Points: XX/18**

### Correctness Summary

Add the points from the summary sections of each problem.

**Points: XX/42**

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

For each of the 4 files submitted:

1: Black reports no formatting changes it would make to the file.

0: Black reports a formatting change it would make to the file.

**Points: XX/4**

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

In `tic_tac_toe.py`:

- `TicTacToeBoard`: **XX/2**
- `__init__`: **XX/2**
- `next_move`: **XX/2**
- `mark`: **XX/2**
- `get_square`: **XX/2**
- `check_win`: **XX/2**
- `__repr__`: **XX/2**

In `user_account.py`:

- `UserAccount`: **XX/2**
- `username`: **XX/2**
- `num_posts`: **XX/2**
- `generate_new_post_id`: **XX/2**

**Points: XX/22**

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

**Points: XX/49**

## Summary

Copy the point totals from each of the four major section summaries above.

**Submission: XX/9**

**Correctness: XX/42**

**Style: XX/49**

### Total

**TOTAL POINTS: XX/100**

### Grader Information

_Grader_:

_Reviewer_:
