import re

def is_valid_email(addr):
    if re.match(r'\w+\.?\w+@\w+\.\w+',addr):
        return True
    if re.match(r'[0-9a-zA-Z.]{1,10}\@\w{2,9}.com',addr):
        return True
    else:
        return False

def name_of_email(addr):
    m=re.match(r'<?(\w+\s?\w+)>?\s?\w*@\w+\.\w+',addr)
    return m.group(1)

print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.com'))
print(is_valid_email('bob#example.com'))
print(is_valid_email('mr-bob@example.com'))
print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.org'))