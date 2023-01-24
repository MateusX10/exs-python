def vote(year_birth):
    from datetime import date
    current_year = date.today().year
    age = current_year - year_birth
    print(f"With {age} anos: ", end='')
    if age < 16:
        print("Cannot vote")

    elif age < 18 or age > 70:
        print("Optional vote")

    else:
        print("Compulsory vote")

print('-=' * 40)
YearOfBirth = int(input("Your year of birth: "))
vote(YearOfBirth)
