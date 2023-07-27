'''translattion between english and franch'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''translation from english to french method'''
    en_fr = MyMemoryTranslator(source='en-GB', target='fr-FR')
    french_text = en_fr.translate(english_text)
    return french_text

def french_to_english(french_text):
    '''translation from french to english'''
    fr_en = MyMemoryTranslator(source='fr-FR', target='en-GB')
    english_text = fr_en.translate(french_text)
    return english_text
