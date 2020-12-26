import re

def emails(data):

    with open(data, 'r') as f:
        file = f.read()
        email_not_duplicated = []
        rouls_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        emails = re.findall(rouls_email, file)
        # we need to sorted all emailes
        emails.sort()
        for email in emails:
            if email not in email_not_duplicated:
                email_not_duplicated.append(email)

        with open('emails.txt', 'w') as w:
            for em in email_not_duplicated:
                w.write(f'{str(em)}\n')    
    
    return email_not_duplicated

def phone_numbers(data):

    with open(data , 'r') as f:
        file = f.read()
        rouls_phone = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        phones = re.findall(rouls_phone , file)
        phones.sort()
        phone_not_duplicated = []

        for phone in phones:
            number_sub = re.sub('[^0-9]+', '', phone)
            number_format = re.sub(r"(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(number_sub[:-1])) + number_sub[-1]

            if number_format not in phone_not_duplicated:
                phone_not_duplicated.append(number_format)

        phone_not_duplicated.sort()
        with open('phone-numbers.txt', 'w') as w:
            for ph in phone_not_duplicated:
                w.write(f'{ph}\n')
    
    return phone_not_duplicated


if __name__ == '__main__':
   print(emails('potential-contacts.txt'))
   print(phone_numbers('potential-contacts.txt'))