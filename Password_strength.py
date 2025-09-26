def strength(password):
    result = []
    for word in password:
        has_letter = False
        has_number = False
        has_symbol = False
        
        length = len(word)
        
        for r in word:
            if ('a' <= r <= 'z') or ('A' <= r <= 'Z'):
                has_letter = True
            elif '0' <= r <= '9':
                has_number = True
            else:
                has_symbol = True
        
        if length < 8 or (has_letter and not has_number and not has_symbol):
            result.append("weak")
        elif length > 12 and has_letter and has_number and has_symbol:
            result.append("strong")
        else:
            result.append("ok")
    return result

print(strength(["abc", "School2025", "L3arn!ngAI2025"]))
# ["weak", "ok", "strong"]
print(strength(["12345", "abcdefg"]))
# ["weak", "weak"]
print(strength(["helloworld", "PythonRocks"]))
# ["weak", "weak"]
print(strength(["abc12345", "Password1", "Hello2025"]))
# ["ok", "ok", "ok"]
print(strength([""]))
# ["weak"]
print(strength(["onlyletters", "Mix123", "GoodOne2023!", "Ultra$trongP@ssw0rd2025"]))
# ["weak", "weak", "ok", "strong"]