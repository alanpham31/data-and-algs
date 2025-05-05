import random
from printOneTest import printOneTest

def randomPermutation(word: str) -> str:
    """
    Generates a random permutation of a given word.
    
    Args:
        word (str): The input string to be permuted.
        
    Returns:
        str: A randomly permuted word.
    """
    length = len(word)
    permuted_word = ""
    used_indices = set()
    
    while len(used_indices) < length:
        random_index = random.randrange(length)
        if random_index not in used_indices:
            permuted_word += word[random_index]
            used_indices.add(random_index)
    
    return permuted_word

def readWords(file_name: str) -> list[str]:
    """
    Reads words from a file, converts them to lowercase, and returns them as a list.
    
    Args:
        file_name (str): The name of the file to read.
        
    Returns:
        list[str]: A list of words in lowercase from the file.
    """
    words = []
    try: 
        with open(file_name, "r") as file:
            line = file.readline()
            while line:
                words.extend(line.strip().lower().split())
                line = file.readline()
    except FileNotFoundError:
        print(f"Error: file not found; {file_name} was not found.")
    return words

def writePermutedWords(new_file_name: str, list_words: list[str]) -> None:
    """
    Writes a random permutation of each word from the given list to a new file, one word per line.
    
    Args:
        new_file_name (str): The name of the output file to write to.
        list_words (list[str]): A list of words to permute and write to the file.
    """
    try:
        with open(new_file_name, "w") as file:
            for word in list_words:
                permuted_word = randomPermutation(word)
                file.write(permuted_word + "\n")
    except IOError as e:
        print(f"Error: cannot write to file '{new_file_name}'. {e}")

def main() -> None:
    # Set the random seed for testing reproducibility
    random.seed(8675309)
    
    # Test 1: Testing randomPermutation function
    print("Testing randomPermutation with input 'frankie':")
    result = randomPermutation("frankie")
    print(f"Result: {result}")
    print(f"Expected: nrekifa\n")
    printOneTest(randomPermutation, "frankie", expected="nrekifa")
    
    # Test 2: Testing readWords function
    print("Testing readWords with input file 'homework1.txt':")
    words = readWords("homework1.txt")
    print(f"Result: {words[:5]}")  # Display the first 5 words for brevity
    print("Expected: A list of lowercase words from the file.\n")
    
    # Test 3: Testing writePermutedWords function
    print("Testing writePermutedWords with input file 'homework1.txt' and output file 'permutedwords.txt':")
    wlist = readWords("homework1.txt")
    writePermutedWords("permutedwords.txt", wlist)
    print("The permuted words have been written to 'permutedwords.txt'.\n")
    
    # Test 4: Another test for writePermutedWords with a different list
    test_words = ["hello", "world", "python", "rocks"]
    print("Testing writePermutedWords with a custom list of words:")
    writePermutedWords("custom_permutedwords.txt", test_words)
    print("The permuted words have been written to 'custom_permutedwords.txt'.\n")

if __name__ == "__main__":
    main()
