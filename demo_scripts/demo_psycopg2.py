import demo_utils

## create todo table

demo_utils.create_table("todo", "id SERIAL PRIMARY KEY, task VARCHAR(255) NOT NULL, status BOOLEAN NOT NULL")

demo_utils.insert_row("todo", "task, status", "'Finish this tutorial', FALSE")

# add random tasks

demo_utils.insert_row("todo", "task, status", "'Buy groceries', FALSE")

demo_utils.insert_row("todo", "task, status", "'Call mom', FALSE")

demo_utils.insert_row("todo", "task, status", "'Do laundry', FALSE")


all_rows = demo_utils.fetch_all("todo")

for row in all_rows:
    print(row)






