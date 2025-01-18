import arabic_reshaper
from bidi.algorithm import get_display

word = "مسح"
reshaped_sentence = arabic_reshaper.reshape(word)
final_sentence = get_display(reshaped_sentence)
print(final_sentence)