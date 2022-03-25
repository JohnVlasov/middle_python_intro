"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        Текст приветствия
    """
    name = ' '.join([word.capitalize() for word in name.split()])
    # Name Full_name
    return 'Привет, {0}'.format(name)
