import sys
from Stack import Stack

def readFile(filename: str) -> str:
    """
    reads contents of file and returns a single string

    parameters:
        filename (str): name of the file to read

    returns:
        str: The contents of the file as a single string

    raises:
        FileNotFoundError: if the file does not exist
    """
    try:
        with open(filename, 'r') as file:
            return file.read().strip() # use .strip to remove leading/trailing whitespace
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    
def main() -> None:
    # main function to read and parse HTML file given

    try:
        # check if filename is given
        if len (sys.argv) < 2:
            raise IndexError("No filename provided")
        
        # read file
        filename = sys.argv[1]
        html_content = readFile(filename)

        # parse HTML
        if parseHTML(html_content):
            print("all tags are properly matched")
        else:
            print("there are mismatched or unmatched tags")
        
    except IndexError as err:
        print(f"error: {err}")
        print("there are mismatched or unmatched tags")
        sys.exit(2)
    except FileNotFoundError as err:
        print(f"error: {err}")
        sys.exit(1)

def parseHTML(html: str) -> bool:
    '''
    parses HTML content and checks if all tags are properly matched'
    
    parameters:
        html (str): HTML content as a string

    returns: 
        bool: true if all tags are properly matched, false otherwise
    '''
    stack = Stack()
    i = 0
    n = len(html)
    empty_tags = {"br", "hr", "img", "input", "link", "meta", "col", "frame", "area", "base", "param"}
    

    while i < n:
        if html[i] == "<":
            if html[i+1] == "/":
                # close tag
                j = html.find(">", i)
                if j == -1:
                    print("invalid HTML: unclosed tag")
                    return False
                tag = html[i+2:j]
                if stack.isEmpty():
                    print(f"unmatched </{tag}")
                    return False
                expected_tag = stack.pop()
                if tag != expected_tag:
                    print(f"mismatched tags: <{expected_tag}> to </{tag}>")
                    return False
                i = j + 1
            else:
                # opening tag or empty tag
                j = html.find(">", i)
                if j == -1:
                    print("invalid HTML: unclosed tag")
                    return False
                tag = html[i+1:j].split()[0] # get tag name, ignore attributes

                if tag in empty_tags or html[j-1] == "/":
                    # empty tag, dont push to stack
                    pass
                else:
                    stack.push(tag)
                i = j + 1

        else:
            i += 1

    if not stack.isEmpty():
        print(f"unmatched tags: {', '.join(f'<{tag}>' for tag in stack._data)}")
        return False

    return True
    
