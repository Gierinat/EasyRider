import re

fields_structure = {'bus_id': {'type': int, 'required': True},
                    'stop_id': {'type': int, 'required': True},
                    'stop_name': {'type': str, 'required': True, 'suffixes': ['Road', 'Avenue', 'Boulevard', 'Street']},
                    'next_stop': {'type': int, 'required': True},
                    'stop_type': {'type': str, 'required': False, 'values': ['S', 'O', 'F', ""]},
                    'a_time': {'type': str, 'required': True}}


def validate_stop_names(field, value):
    capital_letter_start = str(value)[0].isupper() if value else False
    suffix = re.search(r'\w*\b$', str(value))
    suffix = suffix.group() if suffix else None
    allowed_suffixes = fields_structure[field].get('suffixes', None)
    print(suffix, allowed_suffixes)
    if (suffix not in allowed_suffixes) or not capital_letter_start:
        raise StopNameError


def validate_type(field, field_type):
    correct_type = fields_structure[field]['type']
    if correct_type != field_type:
        raise DataTypeMismatchError


def validate_required(field, value):
    is_required = fields_structure[field]['required']
    if is_required and not str(value):
        raise DataRequiredMissing


def validate_value_allowed(field, value):
    allowed_values = fields_structure[field].get('values', None)
    if allowed_values and (value not in allowed_values):
        raise DataValueNotAllowed


class DataValueNotAllowed(Exception):
    pass


class DataRequiredMissing(Exception):
    pass


class DataTypeMismatchError(Exception):
    pass

class StopNameError(Exception):
    pass