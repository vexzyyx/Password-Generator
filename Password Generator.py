import random
import string

def generate_password(
    length=12,
    use_uppercase=True,
    use_lowercase=True,
    use_punctuation=True,
    use_numbers=True,
    use_rare_symbols=True,
):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_punctuation:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_rare_symbols:
        rare_symbols = 'ÆŒẞĄĆĘŁŃÓŚŹŻĎŇŘŠŤŮŽČΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡ΢ΣΤΦΥΨΩαβγδεζηθικλμνξοπρςστυφψωאבגדהויכלמנסעפצקרשת'
        characters += rare_symbols
    if not characters:
        print("You must select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_rare_symbols = input("Include rare symbols? (y/n): ").lower() == 'y'

    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_punctuation=use_punctuation,
        use_numbers=use_numbers,
        use_rare_symbols=use_rare_symbols,
    )

    if password:
        print(f"Generated Password: {password}")
