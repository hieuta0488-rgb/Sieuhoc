# Spec: English units for Vietnamese school grades (GDPT 2018 aligned)

Write ORIGINAL learning content aligned with Vietnam's Chương trình GDPT 2018 môn Tiếng Anh
(themes: Our communities / Our heritage / Our world / Visions of the future at secondary; Me & my friends,
Me & my school, Me & my family, Me & the world around at primary). Do NOT copy any textbook
(Global Success, i-Learn Smart, Explore...) text or exact unit titles; write your own unit titles and content
at the right level for the grade. Vietnamese with full diacritics; explanations child-friendly and short.

Output: one JSON file = array of units, in teaching order. Each unit object:
{
 "id": "en-g<grade>-u<n>",            e.g. "en-g6-u3"
 "grade": <int>,
 "title": "Unit 3: My Friends",         English title (your own)
 "vi": "Bạn bè của em",                 Vietnamese title
 "icon": "👫",                          one emoji
 "goal": "1 câu: học xong em sẽ ...",
 "vocab": [ {"w","ipa","vi","ex","exvi"} ... ],   grade1-2: 6-8 words; g3-5: 8-10; g6-9: 10-14; g10-12: 12-16. IPA General American with slashes.
 "phrases": [ {"en","vi"} ... ],        3-6 useful sentence patterns / dialogue lines for the unit
 "grammar": {"title","content"}        content = short HTML (<p>,<ul><li>,<b>,<table>) with formula + 3-5 examples each with Vietnamese translation;
                                       a tip box as <div class='meo'>Mẹo: ...</div>. Grade 1-2: grammar is just sentence patterns.
 "quiz": [ {"q","opts":[3 or 4],"a":index,"why":"giải thích tiếng Việt ngắn"} ... ]   g1-2: 6; g3-5: 8; g6-12: 10.
         Mix: vocab meaning, fill-in-the-blank grammar, choose correct response, odd-one-out, (g6+) word form, pronunciation (stress/ending sound) items.
}
Validate with Python: valid JSON, ids unique, every "a" in range, options unique within a question, all fields non-empty,
answer keys double-checked. Write with json.dump(ensure_ascii=False, indent=0).
Reply with ONE line: file path, unit count, validation passed.
