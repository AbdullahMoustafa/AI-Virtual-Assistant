#from any langauge to english and it will not be applicable as it will not get any langauge in the 
#regognition function

from googletrans import Translator

# def translateToEnglish(text):
#     translator = Translator()
#     translated = translator.translate(text)

#     print(translated.text)
#     return (translated.text)


def toFrench(text):
    text = text.replace('translate','')
    text = text.replace('to French','')
    translator = Translator()
    translated = translator.translate(text, src='en', dest='fr')
    return (translated.text)

def toGerman(text):
    text = text.replace('translate','')
    text = text.replace('to German','')
    translator = Translator()
    translated = translator.translate(text, src='en', dest='de')
    return (translated.text)

def toSpanish(text):
    text = text.replace('translate','')
    text = text.replace('to Spanish','')
    translator = Translator()
    translated = translator.translate(text, src='en', dest='es')
    return (translated.text)

def toHindi(text):
    text = text.replace('translate','')
    text = text.replace('to Hindi','')
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return (translated.text)

def toItalian(text):
    text = text.replace('translate','')
    text = text.replace('to Italian','')
    translator = Translator()
    translated = translator.translate(text, src='en', dest='it')
    return (translated.text)

def toPortuguese(text):
    text = text.replace('translate','')
    text = text.replace('to Portuguese','')
    translator = Translator()
    translated = translator.translate(text, src='en', dest='pt')
    return (translated.text)

 
# def toChinese(text):
#     text = text.replace('translate','')
#     text = text.replace('to Chinese','')
#     translator = Translator()
#     translated = translator.translate(text, src='en', dest='zh-HK')
#     return (translated.text)