import logging


def get_logger(name):
    # Создание логгера с заданным именем
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Создание форматера
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

    # Создание обработчика, который записывает сообщения в файл
    file_handler = logging.FileHandler('app.log', mode='a', encoding='utf8')
    file_handler.setFormatter(formatter)

    # Создание обработчика, который выводит сообщения в консоль
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Добавление обработчиков к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
