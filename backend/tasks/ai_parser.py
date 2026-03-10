def parse_content(text):
  text = text.lower()

  create_words = [ "create" , "add","need","plan"]
  update_words = ["finished" ,"complete","done","slept"]
  delete_words = ["delete","remove","cancel"]

  for word in create_words:
    if word in text:
      task = text.replace(word,"").strip()

      return {"action" : "create" , "task" : task}
    
    
  for word in update_words:
    if word in text:
      task = text.replace(word,"").strip()

      return {"action" : "update" , "task" : task}
    
    
  for word in delete_words:
    if word in text:
      task = text.replace(word,"").strip()

      return {"action" : "delete" , "task" : task}
    
    
  return {"action" : "create","task" : text}
  #test