"""
Variables for mad libs exercise.
"""

# The original story is not used in the exercise, but included here to show what
# it looked like.
ORIGINAL_STORY = (
    "Olin College is included in Princeton Review's just released Best Value"
    " Colleges for 2020. In addition to the overall listing, Princeton Review"
    " also named Olin as #2 for best classroom experience, #5 for best schools"
    " for internships, #14 for best career services and #18 for best financial"
    " aid. Princeton Review stated that: \"Olin's forward-thinking initiatives,"
    " close student-faculty relationships and emphasis on real-world problems"
    " and solutions prepare students to enter the job market not just as"
    ' valuable employees, but as potential innovators and entrepreneurs."'
)

MAD_LIBS_STORY = (
    "Olin College is included in Princeton Review's just released Best <0-noun>"
    " Colleges for 2020. In addition to the overall listing, Princeton Review"
    " also named Olin as #<1-number> for best <2-noun> experience, #<3-number>"
    " for best schools for <4-plural noun>, #<5-number> for best <6-noun>"
    " services and #<7-number> for best <8-noun>. Princeton Review stated that:"
    " \"Olin's <9-adjective> initiatives, close student-<10-living thing>"
    " relationships and emphasis on real-world problems and <11-plural noun>"
    " prepare students to enter the job market not just as <12-adjective>"
    " <13-plural noun>, but as potential <14-plural noun> and <15-plural"
    ' noun>."'
)

MAD_LIBS_DICT = {
    (0, "noun"): "",
    (1, "number"): "",
    (2, "noun"): "",
    (3, "number"): "",
    (4, "plural noun"): "",
    (5, "number"): "",
    (6, "noun"): "",
    (7, "number"): "",
    (8, "noun"): "",
    (9, "adjective"): "",
    (10, "living thing"): "",
    (11, "plural noun"): "",
    (12, "adjective"): "",
    (13, "plural noun"): "",
    (14, "plural noun"): "",
    (15, "plural noun"): "",
}
