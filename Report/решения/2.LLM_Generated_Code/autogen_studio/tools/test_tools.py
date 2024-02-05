import unittest

import tools_data
import util_read_directory_markdown


# Класс теста, наследующий от unittest.TestCase
class TestAddFunction(unittest.TestCase):

    main_prompt = """
Вы группа исследователей.

Используя предоставленные данные решить следующие задачи:
      * Определить, какие признаки показа являются хорошими предикторами события (например, события fclick), упорядочить их в порядке убывания вместе с численной оценкой их качества
      * Написать код выбора, подбора параметров, обучения и валидации модели классификации на Python, которая прогнозирует вероятность клика на основании информации о показах

Директория с файлами и описанием: 
- ./data

1) для чтения данных используй утилиты из доступных или напиши свои и сохрани их с помощью save_code
2) для обработки данных используй доступные утилиты или напиши свои и сохрани их с помощью save_code
3) для сохранения новых утилит используй save_code
4) для визуализации можешь происледовать библиотеки: plotly, matplotlib seaborn или написать список которые нужно установить

План примерного выполнения задачи:
   1. провести декомпозицию задачи (LLM)
   2. решить исходную или выделенные отдельные задачи последовательно, итеративно или параллельно (LLM)
   3. сгенерировать код на Python, использующий DS/ML frameworks/libs для анализа и визуализации данных и результатов (LLM)
   4. выполнить сгенерированный код (automatic или manual operation)
   5. объединить полученные результаты (automatic или manual operation)
   6. предоставить шаги решения и результаты/ выводы (inferences) системы в форме текстовой и графической информации (automatic или manual operation)
   7. допустимо предварительно обработать исходные данные для решения LLM
   8. допустимо незначительно модифицировать и конкретизировать исходные user prompts для решения LLM, чтобы направить LLM на получение требуемого решения

"""

    def test_read_directory_for_files(self):
        file_paths = tools_data.get_file_paths("/Users/xsa-osx/_projects/1_projects/ALMAGEN/task/data")
        self.assertEqual(len(file_paths) > 0, True)

    def test_read_directory_for_md(self):
        file_paths = util_read_directory_markdown.read_md_files_to_text("/Users/xsa-osx/_projects/1_projects/ALMAGEN/task/data")
        self.assertEqual(len(file_paths) > 0, True)

# Этот код позволяет запустить тесты из командной строки
if __name__ == '__main__':
    unittest.main()