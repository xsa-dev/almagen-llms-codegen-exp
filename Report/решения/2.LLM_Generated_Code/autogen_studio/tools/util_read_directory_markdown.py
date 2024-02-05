import os

def read_md_files_to_text(directory_path):
    """
    Read all markdown (.md) files in the specified directory and return their contents as text.

    Args:
        directory_path (str): The path to the directory containing the markdown files.

    Returns:
        List[str]: A list containing the contents of each markdown file as a string.
    """

    md_texts = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    md_texts.append(str(
                        {'filepath': file_path,
                        'content': md_file.read()}
                        ))

    return md_texts

# Пример использования:
# directory_path = '/path/to/your/markdown/files'
# markdown_texts = read_md_files_to_text(directory_path)
# for text in markdown_texts:
#     print(text)