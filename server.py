"""Модуль управления FastAPI приложением"""
from fastapi import FastAPI

from misc.template_definision import find_matching_template
from misc.type_definition import get_field_type

app = FastAPI()


@app.post("/get_form")
async def get_form(form_data: dict):
    """
        Функция ответа на POST запрос\n

        В формате:\n
        {{\n
            "first_field": "first_value",\n
            "second_field": "second_value"
        }}
    """


    template_name = find_matching_template(form_data)

    if template_name == "Unknown Template":
        field_types = {
            field: get_field_type(form_data[field]) for field in form_data.keys()
            }
        return field_types

    return {"template_name": template_name}
