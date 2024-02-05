import os
from datetime import datetime

def save_code(code, folder='scripts', filename='', ext='py'):
    """Автоматическое сохранение кода в скрипты"""
    
    # Папка для скриптов, если не существует - создаем
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # Имя файла скрипта   
    if not filename:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f'code_{timestamp}'
        
    # Расширение по умолчанию    
    if not ext:
        ext = 'py' 
    
    # Полный путь к файлу    
    filepath = os.path.join(folder, f'{filename}.{ext}')
    
    # Сохранение кода в файл
    with open(filepath, 'w') as f:
        f.write(code)
    
    print(f'Код сохранен в файл: {filepath}')
    
    return filepath