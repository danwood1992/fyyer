import demo_utils

## create todo table

demo_utils.create_table("todo", "id SERIAL PRIMARY KEY, task VARCHAR(255) NOT NULL, status BOOLEAN NOT NULL")

demo_utils.insert_row("todo", "task, status", "'Finish this tutorial', FALSE")



demo_utils.fetch_all("todo")






