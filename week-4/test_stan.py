# text = "I like cats. Cats are cute."

# new_text = text.replace("cats", "dogs")
# print(new_text)   # I like cats. Cats are cute.  (case matters, so "Cats" is not replaced)

# print(text) 

def swap_case(text):
    result = ""
    for char in text:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

text = "Hi"

print(swap_case(text))