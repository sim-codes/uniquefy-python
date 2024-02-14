
def remove_duplicate(filename):
    """
    Removes duplicate numbers from a file.

    Args:
        filename (str): The path to the file.

    Returns:
        list: A list of unique numbers from the file.
    """
    numbers = None
    with open(filename, "r") as reader:
        try:
            lines = reader.readlines()
            numbers = set(lines)
            numbers = list(numbers)
        except Exception as e:
            print(f'Error in reading file: {e}')
    return numbers

def update_file(new_filename, numbers):
    """
    Update the file with the given filename by writing the numbers to it.

    Args:
        new_filename (str): The name of the file to be updated.
        numbers (list): A list of numbers to be written to the file.

    Returns:
        bool: True if the file was successfully updated, False otherwise.
    """
    if not numbers:
        print(f'No numbers to write to {new_filename}')
        return False
    with open(new_filename, "w") as writer:
        for number in numbers:
            number = number.strip()
            writer.write(number + "\n")
    return True

if __name__ == "__main__":
    filename = "test-numbers.txt"
    print(f'Finding unique numbers from {filename}...')
    numbers = remove_duplicate(filename=filename)

    new_filename = "test-unique-numbers.txt"
    updated = update_file(new_filename, numbers)
    if updated:
        print(f'Unique numbers are saved in eca-unique-numbers.txt')
        print(f'Number of unique numbers: {len(numbers)}')
    else:
        print(f'Error in saving unique numbers in eca-unique-numbers.txt')
        