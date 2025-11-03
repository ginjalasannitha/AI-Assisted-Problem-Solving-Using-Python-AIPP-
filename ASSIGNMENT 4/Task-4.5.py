def count_lines_in_file(filename: str) -> int:
    """
    Count the number of lines in a text file.
    Example: 'data.txt' -> 5 lines
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)


if __name__ == "__main__":
    file_name = input("Enter file name: ")
    print("Number of lines:", count_lines_in_file(file_name))
