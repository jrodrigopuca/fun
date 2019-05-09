from translate import Translator

traductor = Translator(from_lang="english", to_lang="spanish")
palabra="hello"
traduccion= traductor.translate(palabra)
print(traduccion)