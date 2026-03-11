from vector_search import find_similarity

tasks = ["sleep at 2","buy groceries","prepare exam"]

user_text = "I slept"

result = find_similarity(user_text,tasks)

print(result)