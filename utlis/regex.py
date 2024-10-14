
import re

def date_formate():
    
    format_date = input("Enter date (dd-mm-yyyy): ")

    # Define the date pattern
    date_pattern = r"(\d{2})-(\d{2})-(\d{4})"  

    # Search for the pattern in the text
    match = re.search(date_pattern, format_date)

    if match:
        # Extract day, month, and year from the match
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))

        # Return the extracted date as a tuple
        return year, month, day
    else:
        return None

# Call the function to extract the date
date = date_formate()

# Output
#if date:
   # print(f"Extracted date: {date[0]:}-{date[1]:02d}-{date[2]:02d}")
#else:
    #print("No date found.")


if __name__ == '__main__':
    date_formate()