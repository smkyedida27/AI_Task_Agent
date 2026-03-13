from sklearn.metrics.pairwise import cosine_similarity

from ai.embeddings import get_embeddings

def find_similarity(user_text,tasks):

  user_vector = get_embeddings(user_text)

  best_score = -1
  best_task = None

  for task in tasks:

    task_vector = get_embeddings(task)

    score = cosine_similarity([user_vector],[task_vector])[0][0]

    if score > best_score:
      best_score = score 
      best_task = task
  
  return best_task
#just to commit