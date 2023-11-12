total = 0 # sum of scores
count = 0 # number of scores entered

# get one score & convert string to integer
score = int(input("Enter score, (Enter -9 to end): ") )

# Add while loop here. Loop while score is not -9
# Add score to total
# Keep a count of scores
# Get next score input

while score != -9:
    total+=score
    print(total)
    count+=1
    score = int(input("Enter score again, (Enter -9 to end): ") )

# print average of scores entered
if count>=1:
    average = float( total ) / count
    print("Class average is", average)
else:
    print("Enter atleast one score except -9")

