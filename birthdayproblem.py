days = 365

for people in range(1, 31):
    probability_different = 1

    for i in range(people):
        probability_different *= (days - i) / days

    probability_same = 1 - probability_different

    print("People:", people)
    print("Probability of same birthday:", probability_same)

    print()

