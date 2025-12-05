file = open('file1.txt')


lines = file.readlines()

# Count the number of lines
line_count = len(lines)

# Print the result
print(f"Total number of lines: {line_count}")
print(lines)