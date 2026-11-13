# Task: remove the "longest option is correct" bias in Ngữ văn quizzes

Files: /tmp/claude-0/school/kntt_van_g<grade>.json (object {"units":[...], "bank":[]}); each unit has "quiz":[{"q","opts":[4],"a","why"}].
Problem: in ~60% of questions the correct option (opts[a]) is the strictly longest one, so pupils can guess.
Do, for every quiz question in your assigned files:
 - KEEP the correct option's meaning; you may shorten/tighten its wording a little.
 - REWRITE the wrong options so they are plausible, clearly wrong for a careful pupil, in the same style, and of
   similar length to the correct one (some longer, some shorter). Never make a wrong option accidentally correct.
 - Do not change q, a (index), why (except to update a quoted option text), ids, or any other field.
Targets per file: correct option strictly longest in ≤ 30% of questions; no question where correct is > 1.4× the next longest.
Write a Python script in your own folder /tmp/claude-0/school/fixlen_<grades>/ that applies your rewrites (by unit id + question index)
and overwrites the file; then validate: valid JSON, 4 unique non-empty options, a in range, same number of units/questions as before,
and print the bias stats before/after. A backup is in /tmp/claude-0/school/backup_van/.
Reply ONE line per file: path, bias before → after, validation passed.
