#!/usr/bin/env python3
import os, sys

path = 'articles/the-bet-against-entropy.html'
with open(path, 'rb') as f:
    raw = f.read()

# Decode with replacement for bad bytes, then write back as clean UTF-8
text = raw.decode('utf-8', errors='replace')
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Fixed: {os.path.getsize(path)} bytes')