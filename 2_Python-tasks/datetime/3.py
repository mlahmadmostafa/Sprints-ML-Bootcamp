import re

# input string
text = "The event is scheduled on 05-01-2025 and another on 15-02-2023"

# regex pattern with capturing groups for DD, MM, YYYY
date_pattern = r'(\d{2})-(\d{2})-(\d{4})'

# find all matches
matches = re.findall(date_pattern, text)

# display extracted dates
extracted_dates = ["-".join(match) for match in matches]
print(extracted_dates)
