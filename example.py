import random
import time

def useLists(num_loops: int, max_value: int) -> tuple[list[int], list[int]]:
    '''
    loop num_loops time, generating ints b/w 1 and max_value inclusive
    Returns:
        two lists: the first is a list of all unique integers generated;
        the second is the corresponding counts of those integers
    '''
    unique = []
    counts = []
    for i in range(num_loops):
        the_int = random.randint(i, max_value)
        if the_int not in unique:
            unique.append(the_int)
            counts.append(1)
        else:
            # find index if the_int and update same spot in counts
            index = unique.index(the_int)
            counts[index] += 1
            
    
    return (unique, counts)



def useDict(num_loops: int, max_value: int) -> dict[int, int]:
    ''' loop num_loops time, generating ints b/w 1 and max_value inclusive
    Returns:
        a dictionary where keys are unique integers generated and corresponding
        values are the counts of those integers
    '''
    dict = {}
    for i in range(num_loops):
        the_int = random.randint(i, max_value)
        if the_int in dict:
            dict[the_int] += 1
        else:
            dict[the_int] = 1 # new key value entry in dict
    return dict
        

def main() -> None:
    ''' 
    - Make sure your two functions produce the same results for small
      values (use seed).
    - Then use large values and time the results of the two different
      approaches (use time.perf_counter).
    - Don't make max_value too big relative to num_loops; o/w, few repeats.
    '''
    random.seed(87654309)
    '''
    unique, counts = useLists(50, 20)
    print(unique, counts)
    print(f"sum of counts = {sum(counts)}")
    '''
    results = useDict(50, 20)
    print(results)

if __name__ == "__main__":
    main()
