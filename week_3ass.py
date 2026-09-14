
# Grade Reporter

scores = [72, 45, 90, 61, 38]


# Go through every score
for score in scores:

    # Work out the grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Count passes and failures
    if score >= 50:
        passed += 1
    else:
        failed += 1

    # Add the score to the running total
    total += score

    # Print the score and grade
    print(f"Score: {score} - Grade: {grade}")

# Calculate the average
average = total / len(scores)

print()
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {round(average, 1)}")