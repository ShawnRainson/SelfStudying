def is_palindrom(text):
    text = str(text)
    text = text.strip()
    text = text.lower()
    text = text.replace(" ", "")
    reverse_text = "".join(reversed(text))
    if text == reverse_text:
        print(True)
    else:
        print(False)

is_palindrom('radar')
is_palindrom('goat')