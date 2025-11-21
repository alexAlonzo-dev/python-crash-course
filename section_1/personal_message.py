person_name = "luz ma"

print(f"Hello {person_name.title()}, do you want to learn something new? ")

print(f"lower case: {person_name.lower()}\nupper case: {person_name.upper()} \ntitle case: {person_name.title()}")

author = "Jorge Luis Borges"
author_quote = '"Hay quienes no pueden imaginar un mundo sin pájaros. Hay quienes no pueden imaginar un mundo sin agua. En lo que a mí se refiere, soy incapaz de imaginar un mundo sin libros"'

print(f"{author} once said, {author_quote} ")

name_strip = "\t\n Alejandro ibarguengoitia \t"
print(f"\nname rstrip: {name_strip.rstrip()} \nname lstrip: {name_strip.lstrip()} \nname fullstrip: {name_strip.strip()}")

url = "https://benditared.com"
print(f"{url.removeprefix("https://")}")
print(f"{url.removesuffix(".com")}")