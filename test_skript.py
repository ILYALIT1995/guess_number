def find_with_substring(t, s):
    rst = []
    for tt in t:
        if s in tt.lower():
            rst.append(tt)
    return rst


original_texts = [
    "Маша читает газету",
    "Кот и кошка гуляют по двору",
    "Бутерброд лежит на столе маслом вниз",
]
what_find = "ма"

print("Подходящие строки:", find_with_substring(original_texts, what_find))
