import hashlib
import sys


def hash_word(word, algorithm="md5"):
    hasher = hashlib.new(algorithm)
    hasher.update(word.encode())
    return hasher.hexdigest()


def crack_hash(target_hash, wordlist, algorithm="md5"):
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            word = line.strip()
            if hash_word(word, algorithm) == target_hash:
                return word
    return None


if __name__ == "__main__":
    if len(sys.argv) not in {3, 4}:
        print("Usage: python hash-cracker.py <hash> <wordlist> [algorithm]")
        sys.exit(1)

    hash_to_crack = sys.argv[1]
    wordlist_file = sys.argv[2]
    selected_algorithm = sys.argv[3] if len(sys.argv) == 4 else "md5"
    result = crack_hash(hash_to_crack, wordlist_file, selected_algorithm)
    if result:
        print(f"Hash cracked! The password is: {result}")
    else:
        print("Password not found in wordlist.")
