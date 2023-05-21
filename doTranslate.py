#!/usr/bin/python3

try:
    import deepl, argparse, clipboard
except ModuleNotFoundError as e:
    print(f"One or more modules not found! Please install module {e.name}")
    exit(1)

# Argparse Stuff
parser = argparse.ArgumentParser()
parser.add_argument("--auth-key", dest="authkey", required=True)
parser.add_argument("--dest-lang", dest="lang", required=True)
args = parser.parse_args()

# Auth Key, clipboard and target language parsing
auth_key = args.authkey
text = clipboard.paste()
target_language = args.lang

# Translating, if not errors
try:
    translator = deepl.Translator(auth_key) 
    result = translator.translate_text(text, target_lang=target_language)
except deepl.exceptions.AuthorizationException as e:
    exit(1)

translated_text = result.text

# Copying back translated stuff to clipboard
clipboard.copy(translated_text)
