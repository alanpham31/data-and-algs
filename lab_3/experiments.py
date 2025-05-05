from List import *
#from progress.bar import Bar  # or choose your favorite
import time
import random

################################################################################
def oneExperiment(list_size: int, prob_remove: float = 0.0) -> dict[str, int]:
    ''' function to conduct one experiment by creating a List object,
        then appending list_size number of integers, with each integer chosen
        at random between 1 and 1000 both inclusive
    Parameters:
        list_size: the size of the List to be created
        prob_remove: probability of removing a random item immediately after
            a new append (i.e., whether, after just appending an item, to
            remove a randomly-selected different item that exists in the list)
    Returns:
        a dictionary of post-experiment stats (see List.py):
            - 'capacity': the resulting internal array capacity (filled and empty)
            - 'resizes': the number of array resizes required across all appends
            - 'append_copies': the number of array-to-array items copied across all appends
            - 'remove_copies': the number of array-to-array items copied as a result of removes 
    '''
    lst = List[int]()
    for i in range(list_size):
        lst.append(random.randint(1, 1000))
        if random.random() < prob_remove and len(lst) > 0:
            index_to_remove = random.randint(0, len(lst) - 1)
            lst.remove(lst[index_to_remove])
    return lst.getInternalStats()

################################################################################
def main() -> None:
    # you will need to add more code throughout below

    random.seed(8675309)
    list_sizes_no_remove   = [10**4, 10**5, 10**6, 10**7]
    list_sizes_with_remove = [10**4, 10**5, 10**6]

    num_experiments_per = 3

    # use references to our advantage in loop below
    list_sizes = list_sizes_with_remove   # or = list_sizes_with_remove

    for list_size in list_sizes:
        print(f'Experimenting with list size {list_size}')
        total_time = 0
        total_capacity = 0
        total_resizes = 0
        total_append_copies = 0
        total_remove_copies = 0

        for i in range(num_experiments_per):
            start_time = time.process_time()
            stats = oneExperiment(list_size)
            elapsed_time = time.process_time() - start_time
            total_time += elapsed_time
            total_capacity += stats["capacity"]
            total_resizes += stats["resizes"]
            total_append_copies += stats["append_copies"]
            total_remove_copies += stats["remove_copies"]

        avg_time = total_time / num_experiments_per
        avg_capacity = total_capacity / num_experiments_per
        avg_resizes = total_resizes / num_experiments_per
        avg_append_copies = total_append_copies / num_experiments_per
        avg_remove_copies = total_remove_copies / num_experiments_per

        print(f"Average time: {avg_time:.4f} seconds")
        print(f"Average capacity: {avg_capacity}")
        print(f"Average resizes: {avg_resizes}")
        print(f"Average append copies: {avg_append_copies}")
        print(f"Average remove copies: {avg_remove_copies}")
        print()

            # conduct one experiment using your function above, keeping track
            # of the returned internal stats to print averages later...
            # remember to use Python's time.process_time to time each
            # experiment individually (starting just before and ending just after 
            # the oneExperiment function call)

if __name__ == "__main__":
    main()
