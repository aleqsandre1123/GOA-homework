
scores_input = input("Enter your scores separated by spaces: ")

scores_list = scores_input.split()

scores_float = [float(score) for score in scores_list]
mean_score = sum(scores_float) / len(scores_float)

print("The arithmetic mean of your scores is:", mean_score)
