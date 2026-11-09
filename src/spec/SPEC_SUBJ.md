# Spec: lessons + graded exercise bank for a Vietnamese school subject (GDPT 2018 aligned)

Write ORIGINAL content in Vietnamese (full diacritics), aligned with Chương trình GDPT 2018 for the subject and grade.
Do NOT copy any textbook (Kết nối tri thức, Chân trời sáng tạo, Cánh Diều) text; write your own explanations/examples.
Math notation: use plain Unicode and simple HTML only (x², x³, √, ∛, π, ≤, ≥, ≠, ×, ÷, ∞, ∫, Σ, ∈, ∅, °, <sup>, <sub>, fractions as a/b or <sup>a</sup>⁄<sub>b</sub>). No LaTeX, no images.

Output ONE JSON object: {"units":[...], "bank":[...]}

UNIT (teaching order, one per main chapter/topic of the grade):
{"id":"<subj>-g<grade>-u<n>","grade":int,"subject":"<subj>","title":"Chương/Chủ đề ...","vi":"one-line Vietnamese subtitle","icon":"one emoji",
 "goal":"Học xong em sẽ ...",
 "theory":"HTML: <h4> sections, <p>, <ul><li>, <b>, <table>; key definitions, rules/formulas in a <div class='meo'>Ghi nhớ: ...</div> box",
 "examples":[{"q":"worked example","giai":"HTML step-by-step solution (Bước 1, Bước 2...)"}],   3-4 per unit
 "quiz":[{"q","opts":[4],"a":index,"why":"giải thích ngắn"}]}                                  8 per unit

BANK item (graded practice with detailed solutions):
{"id":"<subj>-g<grade>-<cb|nc|tinh|qg|olp>-<n>","grade":int,"subject":"<subj>",
 "level":"Cơ bản"|"Nâng cao"|"HSG cấp tỉnh"|"HSG quốc gia"|"Olympic/IOE",
 "skill":"short topic label (e.g. 'Phân số','Phương trình bậc hai','Hình học không gian')",
 "kind":"mc"|"tl", "q":"...", "opts":[4] (mc), "a":index (mc), "ans":"final answer" (tl),
 "giai":"HTML detailed step-by-step solution: phân tích → các bước giải → kết luận (for mc also say why the other options are wrong when useful)",
 "meo":"one-line tip / common trap"}
Difficulty must truly increase. HSG items = genuine competition style (provincial/national gifted-student exams) but original.
Mix: Cơ bản ~90% mc; higher levels ~60% mc / 40% tl.

CORRECTNESS IS CRITICAL: for every numeric/algebraic answer, verify with a Python computation (fractions, sympy if available — pip install sympy is allowed) before writing. Make sure exactly one option is correct.
Validate with Python: valid JSON, unique ids, mc has 4 unique opts and a in range, tl has ans, all fields non-empty.
Write with json.dump(ensure_ascii=False). Reply ONE line: path, units per grade, bank per grade×level, validation passed.
