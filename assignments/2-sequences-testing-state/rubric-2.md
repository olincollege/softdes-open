# Rubric for Assignment 2

## Submission

### Effort

The submission should consist of five files:

- `test_paren_matching.py`
- `paren-matching-report.md`
- `palindrome.py`
- `palindrome-report.md`
- `sequence.py`

For each file:

3: Changes to the file seem to show a good-faith attempt on all problem parts
relating to this file.

2: Changes to the file seem to show a good-faith attempt on at least 50% (but
strictly less than 100%) of problem parts relating to this file.

1: Changes to the file seem to show a good-faith attempt on less than 50% (but
strictly more than 0%) of problem parts relating to this file.

0: The file was unchanged from its initial state.

**Points: XX/15**

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

**Points: XX/18**

## Correctness

### 1. Parenthesis Antithesis

#### Write Unit Tests

This problem has multiple criteria.

##### Enough Unit Tests

1 point per unit test added beyond the original two, up to a maximum of four.

**Points: XX/4**

##### Correct Unit Tests

4 points total. -1 point per test that causes the correct solution to fail, down
to a minimum of 0 points.

**Points: XX/4**

Grader comments: None.

##### Test Justification

1 point per unit test that clearly justifies why it was chosen, up to a maximum
of four.

**Points: XX/4**

Grader comments: None.

##### Write Unit Tests: Total

Add up the points from the previous section.

**Points: XX/12**

#### Determine Correct Implementations

For each of the 14 implementations, the solution should be identified as
correct/incorrect and have an argument for its correctness/incorrectness. An
incorrect implementation should point to a test that identifies it as incorrect,
and a correct implementation should have a good argument for why it is correct.

For every _two_ implementations that are correctly identified _and_ have a
well-reasoned argument for its correctness/incorrectness, give one point.

**Points: XX/7**

##### Grader Comments

_None._

#### Parenthesis Antithesis Summary

Add the points from the previous sections.

**Points: XX/19**

### 2. `next_palindrome(393)` Not Found

#### Bug Watching

For each of the three required additional test cases described, there are 4
points possible:

- The test case either identifies a bug or eliminates a potential bug (1 point).
- The test case substantially differs from the other cases (1 point).
- The written justification for the test case is well-reasoned (2 points).

**Points: XX/12**

Grader Comments: None.

#### A Diagram State of Mind

3: The stack and state diagram is at the line of code containing the bug, and
shows the state of all functions waiting to return.

2: The diagram has minor errors (e.g., close to, but not at, the bug, or missing
some information).

1: The diagram has substantial errors (e.g., shows functions that are not
waiting to return, such as those that have already completed).

0: The diagram is missing or contains little information.

**Points: XX/3**

Grader Comments: None.

#### Fix the Bug

3: The bug is correctly fixed in `palindrome.py` and the report contains a
description of how the change fixes the bug.

2: There is a minor error (e.g., the report does not correctly describe how the
change fixed the bug).

1: There is a major error (e.g., the change does not actually fix the bug).

0: There is no change to the original code, and the section of the report is
missing.

**Points: XX/3**

Grader Comments: None.

#### `next_palindrome(393)` Not Found Summary

Add the points from the previous sections.

**Points: XX/18**

### 3. Read Aloud with Python

#### Docstrings

For each of the two functions (`next_number` and `look_and_say`), give one point
each for the following in the docstring:

- The docstring summarizes what the function does.
- The docstring lists the correct type of the function's parameter.
- The docstring states what the function's parameter represents.
- The docstring lists the correct type and meaning of the function's return, or
  omits this if the function does not return anything.

**Points: XX/8**

Grader Comments: None.

#### Implementation

For each of the two functions (`next_number` and `look_and_say`):

5: The implementation correctly passes all unit tests.

4: The implementation has a minor error (e.g., incorrect return type) but is
otherwise correct.

2: The implementation has a more significant error (e.g., syntax error).

0: The implementation is missing.

**`next_number`: XX/5**

**`look_and_say`: XX/5**

##### Grader Comments

_None._

#### Read Aloud with Python Summary

Add the points from the previous sections.

**Points: XX/18**

### Correctness Summary

Add the points from the summary sections of each problem.

**Points: XX/55**

Grader Comments: None.

## Style

### General

2: The submission contains at most one spelling/grammar mistake.

1: The submission contains a few spelling/grammar mistakes.

0: The submission contains a substantial number of spelling/grammar mistakes.

**Points: XX/2**

Grader Comments: None.

### Git

One point for meeting each of the following criteria (checked over all commits
relevant to the submission):

- The header line of commit message succinctly summarizes what was changed.
- The commit message provides context for the changes made.
- The commit does not contain Git conflict indicators (e.g., `<<<<<<< HEAD`)
  that need to be removed during grading.
- The commit message does not contain lines that exceed 72 characters in length.

**Points: XX/4**

Grader Comments: None.

### Black

For each of the 5 files submitted:

1: Black reports no formatting changes it would make to the file.

0: Black reports a formatting change it would make to the file.

**Points: XX/5**

Grader Comments: None.

### Pylint

Pylint, when run, returns a "style score" out of 10. After running this on all
Python files, take the style score and round it _down_, with minimum of 0
points.

**Points: XX/10**

Grader Comments: None.

### Miscellaneous Code Style

One point per criterion below:

- Variable names follow the course guidelines for formatting and
  descriptiveness.
- The code consistently uses single or double quotes except where it would be
  convoluted to write.
- The code uses Python features taught in class (e.g., f-strings instead of
  `str.format()` or `%`-style strings).
- The code avoids "unpythonic" ways of writing things (e.g., `if x == True`
  instead of `if x`).
- Where needed, there are comments in the code to describe what a block of code
  does (at a high level) or why that code is there.
- The code is generally readable and easy to understand.

**Points: XX/6**

Grader Comments: None.

### Style Summary

Add up the points from all style subsection summaries.

**Points: XX/27**

## Summary

Copy the point totals from each of the major section summaries above.

**Submission: XX/18**

**Correctness: XX/55**

**Style: XX/27**

### Total

**TOTAL POINTS: XX/100**

### Grader Information

_Grader_:

_Reviewer_:
