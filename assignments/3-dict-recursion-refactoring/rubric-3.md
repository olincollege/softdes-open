# Rubric for Assignment 3

## Submission

### Effort

The submission should consist of five files:

- `markov.py`
- `recursive_art.py`
- `portfolio/random.jpg`
- `vote.py`
- `vote-report.md`

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

### 1. Markov Text Generation

The functions for this problem are in `markov.py`.

#### 1.1. Generate the Word List

This step concerns the function `build_word_list`.

3: The function passes all unit tests.

2: The function fails one or more unit tests due to a minor error.

1: The function fails one or more unit tests due to a major error.

0: The function is unchanged or missing.

**Points: XX/3**

Grader Comments: None.

#### 1.2. Build the Dictionary

This step concerns the function `build_next_words`.

7: The function passes all unit tests.

5: The function fails one or more unit tests due to a minor error.

3: The function fails one or more unit tests due to a major error.

0: The function is missing or has a fatal flaw (e.g., syntax error).

**Points: XX/7**

Grader comments: None.

#### 1.3. Generate a Single Sentence

This step concerns the function `generate_sentence`.

3: The function passes all unit tests.

2: The function fails one or more unit tests due to a minor error (e.g., extra
whitespace).

1: The function fails one or more unit tests due to a major error (e.g.,
infinite loop).

0: The function is missing or has a fatal flaw (e.g., syntax error).

**Points: XX/3**

Grader comments: None.

#### 1.4. Generate More Text

This step concerns the function `generate_text`.

3: The function passes all unit tests.

2: The function fails one or more unit tests due to a minor error (e.g., extra
whitespace).

1: The function fails one or more unit tests due to a major error (e.g.,
infinite loop).

0: The function is missing or has a fatal flaw (e.g., syntax error).

**Points: XX/3**

Grader comments: None.

#### Markov Text Generation Summary

Add the points from the previous sections.

**Points: XX/15**

### 2. The Art of Randomness

The submissions for this problem are in `recursive_art.py` and the `portfolio/`
directory.

#### 2.1. Generate Random Art

This step concerns the function `build_random_function`. Testing for this
function is done manually due to the random element.

8: The function passes all tests.

6: The function fails one or more tests due to a minor error.

4: The function fails one or more tests due to a major error.

0: The function is missing or has a fatal flaw (e.g., syntax error).

**Points: XX/8**

Grader comments: None.

#### 2.2. Save Your Artwork

This step concerns the function `portfolio/random.jpg`.

2: The file is an image reasonably matching the images produced by a correct
script.

1: The file is an image, but it does not resemble an image produced by a correct
script (e.g., uniform color, random colors).

0: The file is missing (or unmodified from its original empty file).

**Points: XX/2**

Grader comments: None.

#### The Art of Randomness Summary

Add the points from the previous sections.

**Points: XX/10**

### 3. Alternatives for Alternative Voting

The submissions for this problem are in `vote.py` and `vote-report.md`.

#### 3.1. Refactor Recursively

This step concerns the function `hold_alternative_vote`.

6: The function passes all unit tests.

4: The function fails one or more unit tests due to a minor error.

2: The function fails one or more unit tests due to a major error.

0: The function is missing or has a fatal flaw (e.g., syntax error).

**Points: XX/6**

Grader comments: None.

#### 3.2. Noisrucer: Reflect on Recursion

4: The reflection is well-written and explains why one approach to
implementation was easier to understand or write than the other.

3: The reflection has minor flaws, such as a lack of detail in the response.

2: The reflection either does not mention which implementation was easier to
understand/write, or does not provide justification.

0: The reflection is missing.

**Points: XX/4**

Grader comments: None.

#### Alternatives for Alternative Voting Summary

Add the points from the previous sections.

**Points: XX/10**

### Correctness Summary

Add the points from the summary sections of each problem.

**Points: XX/36**

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

### Docstrings

This section covers docstrings for the functions listed below. For each
function, give one point for each of the following:

- The docstring summarizes what the function does.
- The docstring lists the correct type of the function's parameter.
- The docstring states what the function's parameter represents.
- The docstring lists the correct type and meaning of the function's return, or
  omits this if the function does not return anything.

- `build_word_list`: **XX/4**
- `build_next_words`: **XX/4**
- `generate_sentence`: **XX/4**
- `generate_text`: **XX/4**
- `build_random_function`: **XX/4**

**Points: XX/20**

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

**Points: XX/46**

## Summary

Copy the point totals from each of the four major section summaries above.

**Submission: XX/18**

**Correctness: XX/36**

**Style: XX/46**

### Total

**TOTAL POINTS: XX/100**

### Grader Information

_Grader_:

_Reviewer_:
