# Spec: graded exercise bank WITH DETAILED SOLUTIONS (English, Vietnamese schools, GDPT 2018)

Write ORIGINAL questions (do not copy published exams verbatim; mimic their style and difficulty).
Vietnamese with full diacritics. Output: JSON array of items:
{
 "id": "en-g<grade>-<lvcode>-<n>",          lvcode: cb | nc | tinh | qg | olp
 "grade": <int>, "subject": "en",
 "level": "Cơ bản" | "Nâng cao" | "HSG cấp tỉnh" | "HSG quốc gia" | "Olympic/IOE",
 "skill": short Vietnamese label, e.g. "Ngữ âm","Trọng âm","Từ vựng","Ngữ pháp","Từ loại","Giới từ","Cụm động từ","Đồng/trái nghĩa","Tìm lỗi sai","Viết lại câu","Đọc hiểu","Điền từ đoạn văn","Chia động từ"
 "kind": "mc" (multiple choice) | "tl" (open answer),
 "q": question text. For reading/cloze put the passage inside q (use \n for line breaks; blanks as (1), (2)... and ask ONE question per item, or make the item ask about one blank),
 "opts": [4 options] (only for mc),
 "a": index (only for mc),
 "ans": model answer string (only for tl; for multiple acceptable answers separate with " / "),
 "giai": DETAILED step-by-step solution in Vietnamese as simple HTML (<p>,<b>,<ul><li>,<br>): 
        Bước 1 phân tích dấu hiệu/cấu trúc → Bước 2 loại trừ phương án sai (nói rõ vì sao từng phương án sai) → Kết luận + dịch nghĩa câu.
 "meo": one-line tip (Mẹo nhớ / bẫy thường gặp)
}
Difficulty must really increase by level: HSG items use advanced vocabulary (C1-C2), idioms, collocations,
phrasal verbs, word formation with prefixes/suffixes, complex inversion, guided cloze, error identification in long sentences,
sentence transformation with given word (keyword transformation). QG items are at the level of the Vietnamese national
gifted-student English exam (C1-C2).
Mix ~70% mc, ~30% tl at Nâng cao and above; Cơ bản ~90% mc.
Validate with Python: json valid, ids unique, mc has 4 unique opts and a in range, tl has ans, giai non-empty;
re-check every answer key carefully. Write with json.dump(ensure_ascii=False).
Reply ONE line: path, counts per grade×level, validation passed.
