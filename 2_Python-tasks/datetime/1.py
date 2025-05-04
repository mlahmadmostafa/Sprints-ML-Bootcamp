import re
# Sample text containing email addresses
text = "ahmad@potato.me ibrahim folany matman@super.edu.eg"

# Regular expression to match email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

email_addresses = re.findall(email_pattern, text)
print(email_addresses)

