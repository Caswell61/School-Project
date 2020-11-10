### Author: Nick Caswell
### Program: BNAD 277 Test Statistic Calculator
### Description: Pick which formula to use, then enter
### your numbers.
###
###



# Scipy is used in the zscore function.
import scipy.stats

# This function is for when you know the population standard deviation.
def known():
    sample_mean = float(input("Sample mean:\n"))
    testing_against = float(input("Testing against:\n"))
    observations = float(input("# of observations:\n"))
    pop_deviation = float(input("Population Standard Deviation:\n"))
    square_root = float(observations ** (1 / 2.0))
    test_statistic = float(
        (sample_mean - testing_against) / (pop_deviation / square_root)
    )
    test_statistic = round(test_statistic, 4)
    test_statistic = str(test_statistic)

    print("Your test statistic is:\n" + test_statistic)


# This function is for when you do not know the population standard deviation.
def unknown():
    sample_mean = float(input("Sample mean:\n"))
    testing_against = float(input("Testing against:\n"))
    observations = float(input("# of observations:\n"))
    samp_deviation = float(input("Sample Standard Deviation:\n"))
    square_root = float(observations ** (1 / 2.0))
    test_statistic = float(
        (sample_mean - testing_against) / (samp_deviation / square_root)
    )
    test_statistic = round(test_statistic, 4)
    test_statistic = str(test_statistic)

    print("Your test statistic is:\n" + test_statistic)


# Help function. It'll just be basic information. Might build on it later.
def help():
    print(
        "Not sure what you need help with, this program barely does anything as of right now."
    )
    print(
        "The only thing that this does is give you your test statistic. You're on your own for the rest of it, for now."
    )


# Converts Z-Scores to P-Values and vise versa.
def zscore():
    options = int(
        input(
            """
                        \nPlease select what you'd like to do below:
                        \n1 - Convert P-Value to Z-Score
                        \n2 - Convert Z-Score to P-Value\n"""
        )
    )
    while options not in [1, 2]:
        print("You did not enter a valid option. Please try again.")
        options = int(input(""))
        if options == 1 or options == 2:
            break
    if options == 1:
        pvalue = float(input("What is your P-Value?:\n"))
        print("Your Z-Score is: \n" + str(round(scipy.stats.norm.ppf(pvalue), 3)))
    elif options == 2:
        zscore = float(input("What is your Z-Score?\n"))
        print("Your P-Value is: \n" + str(round(scipy.stats.norm.cdf(zscore), 3)))

# The meat and potatoes. Initial welcome prompt with program's overall logic built into it.
def main():
    print(
        """Please pick from the following options:
    P - Known Population STD
    U - Unknown Population STD
    H - Help
    Z - P-Score - Z-Score Converter
    """
    )

    type_of_problem = input("")

    while type_of_problem.lower() not in {"p", "u", "h", "z"}:
        print("You did not enter a valid input. Please try again.")
        type_of_problem = input("")
        if type_of_problem.lower() in {"p", "u", "h", "z"}:
            break

    if type_of_problem.lower() in {"p"}:
        known()
    elif type_of_problem.lower() in {"u"}:
        unknown()
    elif type_of_problem.lower() in {"z"}:
        zscore()
    elif type_of_problem.lower() in {"h"}:
        help()

    repeating = input("Are you done? (Y/N):\n")

    if repeating.lower() in {"n"}:
        main()
    else:
        print(
            "Cheers! Thanks for using this program. If you want anything added, let me know."
        )


main()
