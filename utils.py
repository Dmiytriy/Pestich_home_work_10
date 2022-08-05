from __future__ import annotations

import json

# Имя JSON-файла с данными кандидатов
CANDIDATES_FILENAME = 'candidates.json'


def load_json(filename: str, encoding: str = 'utf-8'):
    """
    Читает JSON-файл и возвращает список словарей.
    """

    with open(filename, encoding=encoding) as f:
        return json.load(f)


def load_candidates():
    """
    Загружает данные кандидатов из JSON-файла в список словарей.
    """

    return load_json(CANDIDATES_FILENAME)


def get_all(candidates_list: list[dict]):
    """возврат кандидатов на основе списка словарей из JSON файла."""

    result = '<pre>'
    for candidate in candidates_list:
        result += f"""
        Имя кандидата - {candidate['name']}\n
        Позиция кандидата: {candidate['position']}\n
        Навыки: {candidate['skills']}\n
        """
    result += '</pre>'
    return result


def get_by_pk(uid: int):
    """
    Возвращает словарь с данными кандидата по ключу id
    """

    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == uid:
            return candidate
    return None


def get_by_skill(skill: str):
    """
    Возвращает список словарей с данными кандидатов у которых содержится навык, передаваемый аргументом.
    """

    candidates = load_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
