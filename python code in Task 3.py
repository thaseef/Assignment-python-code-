def calculate_monthly_fees(weekly_fees, pch):
    return (4 * weekly_fees) + (pch * 500 * 4)  # Multiply PCH by 4 for a monthly fee

def get_weight_category(weight):
    if weight > 100:
        return "Heavyweight Unlimited"
    elif weight == 100:
        return "Light-Heavyweight"
    elif weight == 90:
        return "Middleweight"
    elif weight == 81:
        return "Light-Middleweight"
    elif weight == 73:
        return "Lightweight"
    elif weight == 66:
        return "Flyweight"
    else:
        return "Below Flyweight"

while True:
    # Step 1: Input athlete details
    name = input("Enter athlete's name: ")

    # Step 2: Input training plan with validation
    training_plan = input("Enter training plan (Beginner/Intermediate/Elite): ").lower()
    if training_plan not in ['beginner', 'intermediate', 'elite']:
        print("Error: Invalid training plan. Please choose Beginner, Intermediate, or Elite.")
        continue

    # Step 3: Determine weekly fees based on training plan
    if training_plan == 'beginner':
        weekly_fees = 2000
    elif training_plan == 'intermediate':
        weekly_fees = 5000
    elif training_plan == 'elite':
        weekly_fees = 7000

    # Step 4: Input athlete weight and validate weight for Intermediate/Elite
    weight = float(input("Enter weight (in kg): "))
    if training_plan in ['intermediate', 'elite'] and weight < 66:
        print("You are not eligible to participate in the competition due to insufficient weight.")
        competition_eligible = False
    else:
        competition_eligible = True

    # Step 5: Input private coaching hours with validation (1-5 hours)
    pch = float(input("Enter private coaching hours (PCH): "))
    if pch < 1 or pch > 5:
        print("Error: Invalid PCH hours. PCH must be between 1 and 5.")
        continue

    # Step 6: Calculate monthly fees
    monthly_fees = calculate_monthly_fees(weekly_fees, pch)

    # Step 7: Private coaching fee
    private_coaching_fee = pch * 500 * 4  # Multiply PCH by 4 to calculate for one month

    # Step 8: Determine competition fees and total fees
    if training_plan != 'beginner':
        participated_before = int(input("How many times have you participated in competitions? "))

        if competition_eligible:
            participate_competition = input("Do you want to participate in the competition? (yes/no): ").lower()

            if participate_competition == 'yes':
                participated_before += 1  # Add 1 if the athlete is participating
                competition_fees = 2500 * participated_before
            else:
                competition_fees = 2500 * participated_before  # Calculate based on previous participation only
        else:
            competition_fees = 2500 * participated_before  # Calculate based on previous participation only

        total_fees = monthly_fees + competition_fees
        weight_category = get_weight_category(weight)
    else:
        competition_fees = 0
        total_fees = monthly_fees
        weight_category = ""

    # Step 9: Output breakdown of costs
    print("\n--- Fee Breakdown ---")
    print(f"Athlete's Name: {name}")
    print(f"Training Plan Fee (Monthly): Rs. {weekly_fees * 4:.2f}")  # Display the monthly training plan fee
    print(f"Private Coaching Fee (Monthly): Rs. {private_coaching_fee:.2f}")
    print(f"Competition Fee: Rs. {competition_fees:.2f}")
    print(f"Total Monthly Fee: Rs. {total_fees:.2f}")

    # Step 10: Option to add another athlete
    another_athlete = input("\nDo you want to enter details for another athlete? (yes/no): ").lower()
    if another_athlete != 'yes':
        break
