import demo_utils

demo_utils.insert_row("persons", "name", "'Don wood'")
demo_utils.insert_row("persons", "name", "'Jason Bourne'")

all_rows = demo_utils.fetch_all("persons")

print(type(all_rows))

for row in all_rows:
    for item in row:
        print(f"{item}, type:{type(item)}")








