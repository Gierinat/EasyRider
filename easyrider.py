import json
import fieldvalidator as fv

bus_str = input()
bus_lines = json.loads(bus_str)
errors = dict()


def main():
    for entry in bus_lines:
        for k, v in entry.items():
            # validating type
            try:
                fv.validate_required(k, v)
                fv.validate_type(k, type(v))
            except (fv.DataRequiredMissing, fv.DataTypeMismatchError):
                errors['total'] = errors.get('total', 0) + 1
                errors[k] = errors.get(k, 0) + 1

    print(errors)


if __name__ == "__main__":
    main()
