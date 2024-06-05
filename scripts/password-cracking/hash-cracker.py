import hashlib
import sys

def crack_hash(hash, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            word = line.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash:
                print(f"Hash cracked! The password is: {word}")
                return
    print("Password not found in wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python hash-cracker.py <hash> <wordlist>")
        sys.exit(1)

    hash_to_crack = sys.argv[1]
    wordlist_file = sys.argv[2]
    crack_hash(hash_to_crack, wordlist_file)
