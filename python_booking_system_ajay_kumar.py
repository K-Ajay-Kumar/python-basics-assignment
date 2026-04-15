# Theatre Booking System

TOTAL_SEATS = 350
remaining_seats = TOTAL_SEATS

total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while True:
    tickets = int(input("Enter number of tickets (0 to exit): "))

    # Exit condition
    if tickets == 0:
        break

    # Validate ticket count
    if tickets < 1 or tickets > 15:
        print("INVALID BOOKING - You can book 1 to 15 tickets only")
        continue

    # Check seat availability
    if tickets > remaining_seats:
        print("BOOKING REJECTED - Not enough seats available")
        rejected_bookings += 1
        continue

    ages = []
    invalid_age = False

    # Input ages
    for i in range(tickets):
        age = int(input(f"Enter age for person {i+1}: "))
        if age < 12:
            invalid_age = True
        ages.append(age)

    # Age validation
    if invalid_age:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1
        continue

    # Booking confirmed
    print(f"BOOKING CONFIRMED - {tickets} tickets")
    total_bookings += 1
    tickets_sold += tickets
    remaining_seats -= tickets

    # Stop if full
    if remaining_seats == 0:
        print("THEATRE FULL")
        break

# Final Report
print("\nFinal Report:")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", remaining_seats)