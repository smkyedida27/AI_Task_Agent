def parse_content(text):
  text = text.lower()

  if "complete" in text:
    return {"action" : "update"}
  elif "delete" in text:
    return {"action" : "delete"}
  
  else:
    return {"action" : "create"}
  