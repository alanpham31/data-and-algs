import random
from printOneTest import printOneTest
'''
used websites: 
    - https://www.w3schools.com/python/ref_random_seed.asp
    - https://stackoverflow.com/questions/22639587/what-does-random-seed-do-in-python
    - https://docs.python.org/3/library/random.html
    - https://stackoverflow.com/questions/72025924/key-shortcut-for-running-python-file-in-vs-code

'''

def randomPermutation(word: str) -> str:
    # generates random permutation of given word
    # parameter(s): word - str, the input string to be permuted
    # return(s): randomly permuted word from given input word
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
    # read file line by line, extract all words, convert to lowercase 
    # and return list of words
    # parameter(s): file_name (str), the name of the file to be rewad
    # return(s): list containing all words in file, converted to lowercase
    words = []
    try: 
        with open(file_name, "r") as file:
            line = file.readline()
            while line:
                words.append(line.strip().lower())
                line = file.readline()
    except FileNotFoundError:
        print("Error: file not found; ", file_name, " was not found.")
    return words

def writePermutedWords(new_file_name: str, list_words: list[str]) -> None:
    # writes random permutation of each word in given list 
    # to a new file with one word per line 
    # parameters: 
    #   new_file_name: the name of the output file to write to (str)
    #   list_words: list of words to permute and write to the file
    try:
        with open(new_file_name, "w") as file:
            for word in list_words:
                permuted_word = randomPermutation(word)
                file.write(permuted_word + "\n")
    except IOError as e:
        print(f"Error: cannot write to file '{new_file_name}'. {e}")

def main() -> None:
    #printOneTest(randomPermutation, "", 0, expected = "")
    random.seed(8675309)
    printOneTest(randomPermutation, "frankie", expected = "nrekifa") #nrekifa = 3164501
    #printOneTest(randomPermutation, "ace   db", 5551212, expected = "a  de c b")
    '''
    testingFunction(randomPermutation, "frankie", 8675309)
    print("Expected: nrekifa")
    testingFunction(randomPermutation, "apple", 42)
    print(randomPermutation("frankie"))

    print(readWords("homework1.txt"))

    # Test 4: Testing writePermutedWords
    wlist = readWords("homework1.txt")
    print("Test 4: Testing writePermutedWords with file 'permutedwords.txt'")
    writePermutedWords("permutedwords.txt", wlist)
    
    # Test 5: Another test for writePermutedWords with a different list
    print("Test 5: Testing writePermutedWords with a different list of words")
    test_words = ["hello", "world", "python", "rocks"]
    '''
main() 
