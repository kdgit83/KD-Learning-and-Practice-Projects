def count_words(file_path):
    # Your code goes here
    count = 0
    with open(file_path, 'r') as file:
        data = file.read()
        words = data.split()
    return len(words)

def create_file(file_path, contents):
    with open(file_path, 'w') as file:
        file.write(contents)

file_path = "article1.txt"
contents = "The movie industry is undergoing significant changes due to new trends, with streaming services making films more accessible to a wider audience."
create_file(file_path, contents)
result = count_words(file_path)
print(result)
