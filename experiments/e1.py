def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest using the formula:
    Simple Interest = (Principal * Rate * Time) / 100
    """
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = calculate_simple_interest(principal, rate, time)


print(f"The Simple Interest is: {simple_interest} for the principal amount of {principal}, at a rate of {rate}%, in a time span of {time} years.")