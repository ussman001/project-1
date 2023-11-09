def main():
    try:
        # Step 1
        kanal1 = float(input("Step 1 - Enter Kanal: "))
        marla1 = float(input("Step 1 - Enter Marla: "))
        square_feet1 = float(input("Step 1 - Enter Square Feet: "))

        # Step 2
        kanal2 = float(input("Step 2 - Enter Kanal: "))
        marla2 = float(input("Step 2 - Enter Marla: "))
        square_feet2 = float(input("Step 2 - Enter Square Feet: "))

        # Calculate the totals
        total_kanal = kanal1 + kanal2
        total_marla = marla1 + marla2
        total_square_feet = square_feet1 + square_feet2

        # Apply the conditions
        if total_marla == 20:
            total_marla = 0
            total_kanal += 1
        
        # Additional condition for Marla > 20
        if total_marla > 20:
            quotient = total_marla // 20
            remainder = total_marla % 20
            total_kanal += quotient
            total_marla = remainder
        
        # Additional condition for Square Feet >= 272
        if total_square_feet >= 272:
            quotient = total_square_feet // 272
            remainder = total_square_feet % 272
            total_marla += quotient
            total_square_feet = remainder

        print(f"Total Kanal: {total_kanal}")
        print(f"Total Marla: {total_marla}")
        print(f"Total Square Feet: {total_square_feet} square feet")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
