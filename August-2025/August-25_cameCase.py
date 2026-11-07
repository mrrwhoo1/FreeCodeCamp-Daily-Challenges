def to_camel_case(text):
    
    text = text.replace("-", " ").replace("_", " ")

   
    words = text.split()

    result = words[0].lower()

    for word in words[1:]:
        result += word.capitalize()

    return result

