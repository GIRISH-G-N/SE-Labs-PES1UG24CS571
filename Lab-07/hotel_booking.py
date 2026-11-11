
def nights_stayed(days):
    if not isinstance(days, str):
        return 0

    try:
        parts = days.split('-')

        if len(parts) != 2:
            return 0

        check_in, check_out = parts

        if not check_in.strip() or not check_out.strip():
            return 0

        check_in = int(check_in.strip())
        check_out = int(check_out.strip())

        if check_in < 1 or check_out < check_in:
            return 0

        return check_out - check_in

    except (ValueError, TypeError):
        return 0


def room_floor(room_code):
    if not isinstance(room_code, str):
        return 0

    try:
        parts = room_code.split('-')

        if len(parts) != 2:
            return 0

        number = parts[1].strip()

        if not number.isdigit():
            return 0

        return int(number[0])

    except (ValueError, TypeError, IndexError):
        return 0


def booking_label(names_csv):
    if not isinstance(names_csv, str):
        return "Unknown +0"

    names = [n.strip() for n in names_csv.split(',')]
    names = [n for n in names if n]

    if not names:
        return "Unknown +0"

    lead = names[0]

    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)


if __name__ == "__main__":
    main()
