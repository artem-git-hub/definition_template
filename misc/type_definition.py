"""Модуль для определения типа"""
import re

def validate_phone(value: str) -> bool:
    """Является ли переданная строчка номером телефона"""
    phone_pattern = re.compile(r'\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}')
    return bool(phone_pattern.fullmatch(value))

def validate_date(value: str) -> bool:
    """Является ли переданная строчка датой"""
    date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$|^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
    return bool(date_pattern.fullmatch(value))

def validate_email(value: str) -> bool:
    """Является ли переданная строчка email-ом"""
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    return bool(email_pattern.fullmatch(value))


def get_field_type(value: str) -> str:
    """Возвращает тип поля по переданному значению"""
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"
