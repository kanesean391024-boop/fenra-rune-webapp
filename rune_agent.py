import random
import os

# Elder Futhark rune mapping
RUNE_MAP = {
    'A': 'ᚨ', 'B': 'ᛒ', 'C': 'ᚲ', 'D': 'ᛞ', 'E': 'ᛖ', 'F': 'ᚠ', 'G': 'ᚷ',
    'H': 'ᚺ', 'I': 'ᛁ', 'J': 'ᛃ', 'K': 'ᚲ', 'L': 'ᛚ', 'M': 'ᛗ', 'N': 'ᚾ',
    'O': 'ᛟ', 'P': 'ᛈ', 'Q': 'ᚲ', 'R': 'ᚱ', 'S': 'ᛊ', 'T': 'ᛏ', 'U': 'ᚢ',
    'V': 'ᚢ', 'W': 'ᚹ', 'X': 'ᛉ', 'Y': 'ᛃ', 'Z': 'ᛉ', 'TH': 'ᚦ'
}

FLAVORS = [
    "Etched in yew and blood: ",
    "Fenra's whisper binds the mist: ",
    "Fenrir's kin carves fate anew: ",
    "Runes awaken, shadows stir: "
]

def translate_to_runes(text):
    """Translate text to Elder Futhark runes."""
    if not text:
        return "No text provided.", ""
    text = text.upper().replace(' ', '')  # Normalize
    result = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i+2] == 'TH':
            result.append(RUNE_MAP.get('TH', ''))
            i += 2
        else:
            char = text[i]
            if char in RUNE_MAP:
                result.append(RUNE_MAP[char])
            i += 1
    runes = ''.join(result) if result else "No valid runes found."
    flavor = random.choice(FLAVORS)
    return runes, flavor

def log_translation(input_text, rune_text, log_file='rune_log.txt'):
    """Log translation to file."""
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"Input: {input_text}\nRunes: {rune_text}\n---\n")
        return True
    except IOError:
        return False

def read_log(log_file='rune_log.txt'):
    """Read the rune log file."""
    try:
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8') as f:
                return f.read().split('\n---\n')[:-1]  # Split entries, skip last empty
        return ["No runes cast yet."]
    except IOError:
        return ["Failed to read rune log."]
