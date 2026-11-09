# Spec: lesson-by-lesson content following the "Kết nối tri thức với cuộc sống" textbook (NXB Giáo dục Việt Nam)

Goal: one entry per LESSON (bài) of the official textbook, in the book's exact order, so a pupil can open
exactly the lesson they study in class. Use the book's real table of contents (Tập 1 / Tập 2, chương, bài titles)
as you best know it. Lesson TITLES and ORDER may follow the book; ALL explanatory text, examples and exercises
must be ORIGINAL (never copy the book's text, examples or exercises).
If you are not sure a lesson title/order matches the current edition, still include your best version and set "chac": 0
(else "chac": 1). Vietnamese with full diacritics. Math notation: Unicode + <sup>/<sub> only, no LaTeX.

Output ONE JSON object {"units":[...], "bank":[]} written with json.dump(ensure_ascii=False). Each unit (one per lesson, plus one
"Ôn tập / Bài tập cuối chương" unit at the end of every chương):
{"id":"<subj>-kntt-g<grade>-b<n>"  (n = running number in book order),
 "grade":int, "subject":"<subj>", "book":"kntt", "tap":1|2,
 "chuong":"Chương I. ...  (or for Văn: 'Bài 1. Tôi và các bạn'; for English: 'Unit 1. My new school')",
 "title":"exact lesson title as in the book, e.g. 'Bài 1. Tập hợp'",
 "vi":"one-line subtitle", "icon":"one emoji", "chac":0|1,
 "goal":"Học xong em sẽ ...",
 "theory":"HTML (<h4>,<p>,<ul><li>,<b>,<table>) concise but complete summary of the lesson's knowledge, with a <div class='meo'>Ghi nhớ: ...</div> box",
 "examples":[{"q","giai"(HTML step-by-step)}]  2–4 per lesson,
 "quiz":[{"q","opts":[4],"a":index,"why"}]   10 per lesson (8 is OK for review units), graded easy→harder, options of similar length,
}
For "Ôn tập cuối chương" units: theory = sơ đồ tóm tắt cả chương; quiz = 12 mixed questions covering the chapter.
CORRECTNESS: verify every computed answer in Python (fractions/sympy; pip install sympy allowed). Exactly one correct option.
Validate with Python: valid JSON, unique ids, mc 4 unique opts & a in range, no empty fields. Work ONLY in your own folder
/tmp/claude-0/school/kntt_<subj>_g<grade>/ for scripts. Reply ONE line: path, number of lesson units, number of review units,
how many have chac=0, validation passed.
