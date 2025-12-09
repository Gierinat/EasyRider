import json
import fieldvalidator as fv

bus_str = input()
bus_lines = json.loads(bus_str)
errors = dict()


def main():
    # checks for errors
    for entry in bus_lines:
        for k, v in entry.items():
            # validating type
            try:
                fv.validate_required(k, v)
                fv.validate_type(k, type(v))
                fv.validate_value_allowed(k, v)
            except (fv.DataRequiredMissing, fv.DataTypeMismatchError, fv.DataValueNotAllowed):
                errors['total'] = errors.get('total', 0) + 1
                errors[k] = errors.get(k, 0) + 1

    # presenting outcomes
    print(f"Type and required field validation: {errors.get('total', 0)} errors")
    for k in fv.fields_structure:
        error = errors.get(k, 0)
        print(k, ": ", error, sep="")


if __name__ == "__main__":
    main()
