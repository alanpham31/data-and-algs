import random
from printOneTest import printOneTest

def randomPermutation(word: str) -> str:
    # generates random permutation of given word
    # parameter(s): word (str); input string to be permuted
    # return(s): randomly permuted word from given input word
    length = len(word)
    permuted_word = ""
    used_index = set()

    while len(used_index) < length:
        random_index = random.randrange(length)
        if random_index not in used_index:
            permuted_word += word[random_index]
            used_index.add(random_index)
    return permuted_word

def main() -> None:
    random.seed(8675309)
    printOneTest(randomPermutation, "frankie", expected = "nrekifa")
main()