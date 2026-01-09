import json
import fieldvalidator as fv

bus_str = input()
bus_lines = json.loads(bus_str)
errors = dict()


def main():
    # checks
    for entry in bus_lines:
        for k, v in entry.items():
            # validating Type + allowed values
            try:
                fv.validate_required(k, v)
                fv.validate_type(k, type(v))
                fv.validate_value_allowed(k, v)
            except (fv.DataRequiredMissing, fv.DataTypeMismatchError, fv.DataValueNotAllowed):
                errors['total'] = errors.get('total', 0) + 1
                errors[k] = errors.get(k, 0) + 1

            # validating Format
            try:
                if k == 'stop_name':
                    fv.validate_stop_names(k, v)
                if k == 'a_time':
                    fv.validate_time(k, v)
            except (fv.StopNameError, fv.TimeFormatError):
                errors['total'] = errors.get('total', 0) + 1
                errors[k] = errors.get(k, 0) + 1

    # gathering stats
    buses = dict()
    for entry in bus_lines:
        bus_id = entry["bus_id"]
        buses.setdefault(bus_id, []).append({k: v for k, v in entry.items() if k != "bus_id"})


    # presenting outcomes
    print(f"Type and required field validation: {errors.get('total', 0)} errors")
    for k in fv.fields_structure:
        error = errors.get(k, 0)
        print(k, ": ", error, sep="")

    print("\nLine names and number of stops:")
    for k, v in buses.items():
        print("bus_id: ", k, " stops: ", len(v), sep="")


if __name__ == "__main__":
    main()
