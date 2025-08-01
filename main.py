from password_strength_checker import password_checker

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    strength, suggestions = password_checker(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for tip in suggestions:
            print(f" - {tip}")

if __name__ == "__main__":
    main()
