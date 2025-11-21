name = "ada lovelace"

print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print("\tPython tab")
print("\nProgramming Languages: \n\tJava\n\tPython\n\tC++")

favorite_language = "  JAVA   "
print(f"\nRight Strip: \n{favorite_language.rstrip()}")
print(f"\nLeft Strip: \n{favorite_language.lstrip()}")
print(f"\nFull Strip: \n{favorite_language.strip()}")

benditared_url = "https://benditared.com"
print(benditared_url.removeprefix("https://"))