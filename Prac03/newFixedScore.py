def main():
    scorecheck = False
    while not scorecheck:
        try:
            score = float(input("Enter score: "))
            scorecheck = True
            calculate_grade(score)
        except ValueError:
            print("Please enter a valid integer.")

def calculate_grade(score):
    if score < 0 or score > 100:
        result = print("Invalid score")
        return result
    elif score >= 50 and score <= 90:
        result = print("Passable")
        return result
    elif score > 90:
        result = print("Excellent")
        return result
    else:
        result = print("Bad")
        return result

main()
