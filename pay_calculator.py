def calculate_pay(hours, hourly_rate):
    return round(hours * hourly_rate, 2)

def main():
    print("Shift Pay Calculator")
    rate = float(input("Hourly rate (£): "))
    total = 0

    while True:
        entry = input("Hours worked this shift (or 'done' to finish): ")
        if entry.lower() == "done":
            break
        try:
            hours = float(entry)
        except ValueError:
            print("Please enter a number.")
            continue
        pay = calculate_pay(hours, rate)
        total += pay
        print(f"This shift: £{pay}")

    print(f"Total pay: £{round(total, 2)}")

main()
