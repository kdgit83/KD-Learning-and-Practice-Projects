def main():
    """Generate a band name based on user's city and pet."""
    print("Welcome to the Band Name Generator.\n")
    city = input("What's the name of the city you grew up in?\n==> ")
    pet = input("What's your pet's name?\n==> ")
    band_name = f"\"{city} {pet}\""
    print(f"\nYour band name could be: {band_name}")


if __name__ == "__main__":
    main()
