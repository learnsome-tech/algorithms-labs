import hashlib

def stable_hash(text, width=16):
    return hashlib.sha256(text.encode()).hexdigest()[:width]

print(stable_hash('apple'))
print(stable_hash('banana'))
print(stable_hash('apple'))
print(stable_hash('Apple'))
