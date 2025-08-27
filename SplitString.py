my_sentence = "Anan and Benjawan want to play badminton before dinner"

lower_sentence = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz"
)

lower_mysentence = my_sentence.translate(lower_sentence)

oneword = ""
words = []
for char in lower_mysentence:
    if char != " ":
        oneword += char
    else:
        words.append(oneword)
        oneword = ""
        
words.append(oneword)
        
for oneword in words:
    print(oneword)
    
print(len(words))

"""_summary_
วิธีแปลงตัวอักษรเป็น lowercase 
1. ใช้ .maketran() คู่กับ .translate
2. ใช้ การวนลูปและใช้รหัส ASCII
3. ง่ายสุด lower()

การวนลูปและใช้รหัส ASCII
    text = "Hello World"
    lowercase_text = ""

    for char in text:
        # ตรวจสอบว่าตัวอักษรเป็นตัวพิมพ์ใหญ่หรือไม่
        # ord(char) จะแปลงตัวอักษรให้เป็นรหัส ASCII
        if 'A' <= char <= 'Z':
            # ถ้าเป็นตัวพิมพ์ใหญ่ ให้บวก 32 เข้าไปในรหัส ASCII เพื่อแปลงเป็นตัวเล็ก
            lowercase_char = chr(ord(char) + 32)
            lowercase_text += lowercase_char
        else:
            # ถ้าไม่ใช่ตัวพิมพ์ใหญ่ (เช่น ตัวเล็ก, ตัวเลข, หรือสัญลักษณ์อื่น ๆ)
            # ให้เก็บตัวอักษรนั้นไว้เหมือนเดิม
            lowercase_text += char

    print(lowercase_text)
    # ผลลัพธ์: hello world
    
ใช้ .maketran() คู่กับ .translate    
    .maketrans() กับ .translate() ใช้คู่กันเสมอครับ เปรียบเสมือนสองขั้นตอนในกระบวนการเดียวกัน:
    str.maketrans(): ทำหน้าที่ สร้างตารางกฎ ว่าจะให้ตัวอักษรใดแปลงเป็นตัวอักษรใด . คุณต้องสร้างตารางนี้ก่อน
    .translate(table): ทำหน้าที่ ใช้กฎ ที่สร้างไว้จากขั้นตอนแรก เพื่อนำไปแปลงข้อความจริง ๆ ครับ
        
"""