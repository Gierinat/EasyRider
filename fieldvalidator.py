fields_structure = {'bus_id': {'type': int, 'required': True},
                    'stop_id': {'type': int, 'required': True},
                    'stop_name': {'type': str, 'required': True},
                    'next_stop': {'type': int, 'required': True},
                    'stop_type': {'type': str, 'required': False, 'values': ['S', 'O', 'F', ""]},
                    'a_time': {'type': str, 'required': True}}


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
