INITIAL_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WORD_DICTIONARY = set(open("assets/cleaned_dict.txt", "r").read().upper().splitlines())

def solve_cipher(cipher: str) -> list[tuple[str, int, int, float]]:
    results = []
    for key in range(26):
        decrypted_text = ""
        for char in cipher:
            if char.isalpha():
                if char.isupper():
                    decrypted_text += INITIAL_CHARACTERS[(INITIAL_CHARACTERS.index(char) - key) % 26]
                else:
                    decrypted_text += INITIAL_CHARACTERS[(INITIAL_CHARACTERS.index(char.upper()) - key) % 26].lower()
            else:
                decrypted_text += char
        
        score = calculate_score(decrypted_text)
        accuracy = calculate_similarity(cipher, decrypted_text)
        results.append((decrypted_text, key, score, accuracy))
    
    return sorted(results, key=lambda x: (x[2], x[3]), reverse=True)

def calculate_score(text: str) -> int:
    words = text.split()
    score = 0
    
    for word in words:
        word = word.upper()  # Convert word to uppercase for dictionary matching
        
        # Check for whole word in the dictionary
        if word in WORD_DICTIONARY:
            score += len(word)  # Give more weight to longer words
        
        # Check for substrings in the word
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                substring = word[i:j]
                if substring in WORD_DICTIONARY and len(substring) > 1:
                    score += 1

    return score

def calculate_similarity(cipher: str, decrypted_text: str) -> float:
    total_chars = len(cipher)
    different_chars = sum(1 for c, d in zip(cipher, decrypted_text) if c != d)
    return ((total_chars - different_chars) / total_chars) * 100 if total_chars > 0 else 0.0

def main():
    cipher = input("Enter the cipher to solve: ")
    decrypted_results = solve_cipher(cipher)
    top_result = decrypted_results[0]
    print(f"Decrypted Text: {top_result[0]}")
    print(f"Similarity: {top_result[3]:.2f}% | Key: {top_result[1]} | Score: {top_result[2]}")

if __name__ == "__main__":
    main()