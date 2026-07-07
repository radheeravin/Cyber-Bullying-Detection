
import os

LEXICON_FILE = 'backend/lexicon_data.txt'

# Categories and keywords
PATTERNS = {
    'Violence/Threat': ['kill', 'die', 'murder', 'rape', 'shoot', 'gun', 'knife', 'bomb', 'attack', 'terrorist', 'blood', 'behead', 'assassinate'],
    'Hate Speech': ['nigger', 'fag', 'retard', 'spastic', 'tranny', 'negro', 'dyke', 'kike', 'chink', 'wetback', 'gook', 'hymie', 'sambo', 'wop', 'polack', 'jew', 'whitey', 'gypsy', 'cripple'],
    'Sexual Harassment': ['slut', 'whore', 'dick', 'cock', 'pussy', 'vagina', 'tit', 'boob', 'sex', 'porn', 'nude', 'virgin', 'anal', 'oral', 'cum'],
    'Insult/Bullying': ['stupid', 'idiot', 'dumb', 'loser', 'trash', 'ugly', 'fat', 'clown', 'fool', 'suck', 'crap', 'bitch', 'bastard', 'ass', 'shit', 'fuck', 'damn', 'jerk', 'creep', 'lazy', 'crazy', 'insane']
}

def get_category_and_weight(word, current_weight):
    word = word.lower()
    
    # Check strict matches first
    for cat, keywords in PATTERNS.items():
        if any(k in word for k in keywords):
            # Fine-tune weight based on severity of category
            if cat == 'Violence/Threat': return 0.9, cat
            if cat == 'Hate Speech': return 1.0, cat
            if cat == 'Sexual Harassment': return 0.8, cat
            if cat == 'Insult/Bullying': return 0.6, cat
            
    # Default fallback
    return current_weight, "General Abusive"

def upgrade():
    if not os.path.exists(LEXICON_FILE):
        print("Lexicon file not found.")
        return

    new_lines = []
    with open(LEXICON_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                word = parts[0]
                try: weight = float(parts[1])
                except: weight = 0.5
                
                # Apply categorization logic
                new_weight, category = get_category_and_weight(word, weight)
                
                # Emojis (if not caught by above)
                if word and ord(word[0]) > 127: # Basic Check for non-ascii/emoji
                    category = "Abusive Symbol/Emoji"
                
                new_lines.append(f"{word},{new_weight},{category}")
                
    with open(LEXICON_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines))
        
    print(f"Upgraded {len(new_lines)} lexicon entries.")

if __name__ == "__main__":
    upgrade()
