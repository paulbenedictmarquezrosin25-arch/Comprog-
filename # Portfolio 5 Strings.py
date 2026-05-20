# Portfolio 5 Strings 

# this code is about applying the concepts of strings in daily life activities, specifically calisthenic workout

# input of the user requires the name of the exercise you want to track
workexercise = input("Enter your main exercise (e.g. Push-ups, Pull-ups, Dips, etc.): ")

exercise = workexercise.strip().lower() # this function removes the spaces within the input and standardizes it 

# code that identifies the target of muscle based on the input of the user
if "pull" in exercise or "chin" in exercise:
    targetmuscle = "back and biceps"
elif "push" in exercise or "dip" in exercise:
    targetmuscle = "chest and triceps"
elif "lunge" in exercise or "squat" in exercise:
    targetmuscle = "legs"
else:
    targetmuscle = "full body or core"

print(f"Targeting: {targetmuscle}")

#this converts the number of sets and reps the user plans to do, in order to calculate the inputs mathematically
setinput = input("Enter the number of sets you plan to do: ")
set = int(setinput) # converts the input string to an integer

repinput = input("Enter the number of reps you plan to do per set: ")
rep = int(repinput) # converts the input string to an integer

totalreps = set * rep # calculates the total number of reps by multiplying sets and reps

print(f"Total reps planned: {totalreps}")

#concatenating strings using the + operator to build a log entry
log_entry = exercise.upper() + " Done!"
print("\n" + log_entry)
print("Total repetitions accumulated: " + str(totalreps))

# Slicing a string to extract a shorthand routine code
# Extracts the first 3 letters of the exercise as a workout code
exercise_code = exercise[0:3].upper()
print(f"Saved to log under routine code: {exercise_code}")

# Looping through a string to create a visual intensity bar
print("\nWorkout Intensity Metaphor:")
# Counts how many letters are in the name to determine intensity length
for letter in exercise:
    # Prints a muscle emoji for every letter in the exercise name
    print("💪", end="")
print(" (Based on name length)")