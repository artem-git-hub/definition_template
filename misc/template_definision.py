"""Определение шаблона"""

from db.mongo_service import get_coolections
from misc.type_definition import get_field_type

def get_template_name(template: dict) -> str:
    """Возвращает тип шаблона"""

    return template.get("template_name", "Unknown Template")



def find_matching_template(form_data: dict) -> str:
    """Поиск в БД подходящих шаблонов"""

    templates_collection = get_coolections()

    for template in templates_collection.find():

        template_fields = {field: template["fields"][field] for field in template["fields"].keys()}

        if set(template_fields.keys()).issubset(form_data.keys()):

            if all(get_field_type(form_data[field]) == template_fields[field] for field in template_fields.keys()):
                return get_template_name(template)
    
    return "Unknown Template"
