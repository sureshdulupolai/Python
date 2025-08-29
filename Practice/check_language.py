from deep_translator import GoogleTranslator

text = "Suresh Polai"
translated_text = GoogleTranslator(source="en", target="hi").translate(text)

# print("English:", text)
print("Hindi:", translated_text)

