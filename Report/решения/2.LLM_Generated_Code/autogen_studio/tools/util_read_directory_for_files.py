import os

def get_file_paths(directory_path):
    """
    Reads a directory and returns file paths to all files within the directory and its subdirectories.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        List[str]: A list of file paths.

    Example:
        >>> file_paths = get_file_paths('/path/to/directory')
        >>> for path in file_paths:
        ...     print(path)
    """

    file_paths = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return file_paths

# Example usage:
# file_paths = get_file_paths('/path/to/your/directory')
# print(file_paths)