# module_00.py
# a small program that collects, classifies, validates and prints your name and age.

# print statement to confirm __main__
# print(f"module_00 __name__ = {__name__!r}")

def read_age():
    age_text = input("How old are you? ")

    while not age_text.isdigit(): 
        print("Error: enter your age using digits only.")
        age_text = input("Try again dummy, what is your age: ")
    
    return int(age_text)

def classify_age(age):
    if age < 18:
        return "a minor"
    elif age < 65:
        return "an adult"
    else:
        return "a senior"

def build_summary(name, age):
    age_group = classify_age(age)
    
    return(
        f"Hello, {name}, you are {age_group}.\n"
        f"You are {age}, and next year you will be {age + 1}."
    )

expected_summary = (
    "Hello, Travis, you are an adult.\n"
    "You are 27, and next year you will be 28."
)

actual_summary = build_summary("Travis", 27)

assert actual_summary == expected_summary
assert classify_age(17) == "a minor"
assert classify_age(18) == "an adult"
assert classify_age(64) == "an adult"
assert classify_age(65) == "a senior"

if __name__ == "__main__":
    name = input("What is your name? ")
    age = read_age() 
    summary = build_summary(name, age)

    print(summary)
