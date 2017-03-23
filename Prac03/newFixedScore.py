def main():
    check_score = False
    while not check_score:
        try:
            score = float(input("Enter score: "))
            check_score = True
            print(calculate_grade(score))
        except ValueError:
            print("Please enter a valid integer.")


def calculate_grade(score):
    if score < 0 or score > 100:
        result = "Invalid score"
        return result
    elif 90 >= score >= 50:
        result = "Passable"
        return result
    elif score > 90:
        result = "Excellent"
        return result
    else:
        result = "Bad"
        return result


main()
