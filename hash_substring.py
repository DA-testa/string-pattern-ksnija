# python3
# Ksenija Žuka, 18.gr, 221RDC024

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().strip()
    if 'I' in input_type:
        pattern = input().strip()
        text = input().strip()
    elif 'F' in input():
        with open("tests/06") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    patHash = sum(ord(c) for c in pattern) % 101
    textHash = sum(ord(text[i]) for i in range(len(pattern))) % 101
    occurances = []

    for i in range(len(text) - len(pattern) + 1):
        if patHash == textHash:
            if pattern == text[i:i+len(pattern)]:
                occurances.append(i)
        if i<len(text) - len(pattern):
            textHash = textHash - ord(text[i]) + ord(text[i+len(pattern)])
            textHash %= 101
    # and return an iterable variable
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

