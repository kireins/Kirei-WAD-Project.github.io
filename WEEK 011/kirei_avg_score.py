def count_average():
    # Input student score
    student_total = int(input("How many is your student? : "))

    # Store the given score
    score_total = 0

    # Make list 
    for i in range(student_total):
        # Get input score form user 
        score = float(input(f"Student score-{i + 1}: "))
        
        # add score to total score 
        score_total += score

    # calculate average of the student score 
    average = score_total / student_total

    # result
    print(f"The average score is: {average}")

def main():
    # call the calculation 
    count_average()

# Run the main function
if __name__ == "__main__":
    main()
