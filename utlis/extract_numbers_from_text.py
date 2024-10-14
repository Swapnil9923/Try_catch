



def extract_numbers_from_text(text):  

    numbers = []
    for word in text.split():

      if word.isdigit():
          numbers.append(int(word))
    return {
        'status': 'success',
        'result': numbers
    }



