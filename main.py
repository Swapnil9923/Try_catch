


from utlis.extract_numbers_from_text import extract_numbers_from_text
from utlis.customdate import convert_date
from utlis.regex import date_formate

def main():
    print('main function')

    text = 'I have 4 apples and 6 oranges'  
    result = extract_numbers_from_text(text)
    print(f"Extracted numbers: {result}")

    print()

    
    date_format = input('Enter date (dd-mm-yyyy): ')
    converted_date = convert_date(date_format)
    print(f'Converted Date: {converted_date}')

    print()
    
    date = date_formate()
    if date:
        print(f"Extracted date: {date[0]}-{date[1]:02d}-{date[2]:02d}")
    else:
        print("No date found.")



if __name__ == "__main__":
    main()
