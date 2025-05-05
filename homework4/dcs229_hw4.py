import sys
import random
import time

def main():
    # check if right # of args is given
    if len(sys.argv) != 5:
        print("Usage: python hw4.py [# replications] [# appends] [append option: (a) .append (b) += (c) +]  [seed]")
        sys.exit(0)
    
    try:
        # go though command-line args
        replications = int(sys.argv[1])
        appends = int(sys.argv[2])
        append_option = sys.argv[3].lower()
        seed = int(sys.argv[4])

        # append option
        if append_option not in ["a", "b", "c"]:
            raise ValueError("Append option has to be 'a', 'b', 'c'.")
        
    except ValueError as error:
        print(f"Invalid input: {error}")
        print("Usage: python hw4.py [# replications] [# appends] [append option: (a) .append (b) += (c) +]  [seed]")
        sys.exit(0)
    
    # set random seed
    random.seed(seed)

    # initialize total time
    total_time = 0.0

    # start replications
    for i in range(replications):
        my_list = [] # create empty list

        # start time
        start_time = time.process_time()

        # start appends
        for i in range(appends):
            new_int = random.randint(1, 999999)

            if append_option == "a":
                my_list.append(new_int)
            elif append_option == "b":
                my_list += [new_int]
            elif append_option == "c":
                my_list = my_list + [new_int]

        # end time
        end_time = time.process_time()
        total_time += (end_time - start_time)
    
    # calc avg time
    average_time = total_time / replications

    # results
    print(f"Using seed {seed}, for {replications} replications of {appends} appends each,")
    print(f"the average loading time using append option {append_option} is {average_time:.4f} seconds")

if __name__ == "__main__":
    main()