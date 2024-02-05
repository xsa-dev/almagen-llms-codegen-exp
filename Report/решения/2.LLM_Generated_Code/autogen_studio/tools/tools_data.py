def load_files_from_directory(directory_path='data', max_files=10):

    """
    Loads files from the specified directory, caches their contents, and returns the content.
    
    Args:
        directory_path (str): The path to the directory containing the files.
        max_files (int, optional): The maximum number of files to load. Defaults to 10.
        
    Returns:
        file_contents (list): A list of strings, where each string is the content of a file.
        
    Example:
        >>> contents = load_files_from_directory("/path/to/directory")
        >>> print(contents[0])  # Print the content of the first file
    """
    import os
    import json
    import hashlib
    
    # Create a unique key for caching based on the directory path and the max_files parameter
    key = hashlib.md5((directory_path + str(max_files)).encode("utf-8")).hexdigest()
    cache_dir = ".cache"
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)

    # Cache file name
    fname = os.path.join(cache_dir, key + ".cache")

    # Cache hit
    if os.path.isfile(fname):
        with open(fname, "r", encoding="utf-8") as fh:
            data = json.loads(fh.read())
            return data

    # Load up to max_files from the directory
    file_contents = []
    for root, dirs, files in os.walk(directory_path):
        for file in files[:max_files]:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as file_handle:
                file_contents.append(file_handle.read())

            # If we have read the maximum number of files, stop
            if len(file_contents) >= max_files:
                break
        # If we have read the maximum number of files, stop
        if len(file_contents) >= max_files:
            break

    # Save to cache
    with open(fname, "w") as fh:
        fh.write(json.dumps(file_contents))

    return file_contents

def fill_missing(df, columns, value):
    """Заполнение пропущенных значений"""
    for col in columns:
        df[col].fillna(value, inplace=True)
        
def filter_outliers(df, columns, sd=3):
    """Удаление выбросов по правилу 3 сигм"""
    for col in columns:
        mean, std = df[col].mean(), df[col].std()
        cut_off = std * sd
        lower, upper = mean - cut_off, mean + cut_off
        df = df[(df[col] > lower) & (df[col] < upper)]
    return df
  
def encode_categorical(df, columns):
    """Кодирование категориальных признаков"""
    for col in columns:
        df[col] = df[col].astype('category').cat.codes
    return df