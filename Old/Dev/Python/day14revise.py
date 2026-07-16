def count_words(text):
    count = {}
    if isinstance(text, str):
        sep_text = text.split(' ')
        for el in sep_text:
            count[el] = count.get(el, 0) + 1
        print(f'Counts: {count}')
    else:
        count = {}
        print(count)

count_words('banana apple orange apple banana')

