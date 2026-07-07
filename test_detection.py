
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

import preprocessing
import lexicon
import heuristic_context
import fusion

# Test cases
tests = [
    "You are an idiot",
    "I will kill you",
    "This is stupid",
    "I hate you",
    "Have a nice day",
    "Don't be silly",
    "You are ugly and fat"
]

print(f"{'Text':<30} | {'LIS':<6} | {'CAS':<6} | {'HCS':<6} | {'Decision'}")
print("-" * 70)

for text in tests:
    clean = preprocessing.preprocess(text)
    
    # 1. Lexicon
    lis, count, cats = lexicon.calculate_LIS(clean)
    
    # 2. Context
    abusive_tokens = [t for t in clean.split() if t in lexicon.LEXICON_DB]
    cas = heuristic_context.analyze_context(clean, abusive_tokens)
    
    # 3. Fusion (Using current app.py settings: Alpha=0.5, Threshold=0.6)
    alpha = 0.5
    hcs, decision = fusion.calculate_HCS(lis, cas, alpha=alpha, threshold=0.6)
    
    print(f"{text:<30} | {lis:.4f} | {cas:.4f} | {hcs:.4f} | {decision}")
