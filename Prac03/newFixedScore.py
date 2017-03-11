def main():
    score = float(input("Enter score: "))
    parameter_sort(score)
#TODO Integer Checking
#while score != score.is_integer():
    #float(input("Enter score: "))

def parameter_sort(score):
    if score < 0 or score > 100:
        result = print("Invalid score")
        return result
    elif score > 50 and score <= 90:
        result = print("Passable")
        return result
    elif score > 90:
        result = print("Excellent")
        return result
    else:
        result = print("Bad")
        return result

main()
