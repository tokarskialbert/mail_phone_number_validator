import re

menu_index = -1


def phone_number_validator(phone_nr):
    pattern1 = re.compile(r"[\d]{3} [\d]{3} [\d]{3}")
    pattern2 = re.compile(r"[\d]{9}")
    pn_first_two_official = ['50', '51', '53', '57', '60', '66', '69', '72', '73', '78', '79', '88']
    my_first_two = phone_nr[:2]

    if re.fullmatch(pattern1, phone_nr) or re.fullmatch(pattern2, phone_nr):
        if my_first_two in pn_first_two_official:
            print(f"'{phone_nr}' to PRAWIDŁOWY numer telefonu")
        else:
         print(f"'{phone_nr}' to NIEPRAWIDŁOWY numer telefonu. Spróbuj jeszcze raz.")
    else:
        print("Podany numer telefonu nie składa się z odpowiedniej liczby cyfr lub został podany w złym formacie. Spróbuj jeszcze raz. ")


def email_validator(email1):
    mail_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    if re.fullmatch(mail_pattern, email1):
        print(f"'{email1}' to PRAWIDŁOWY adres e-mail.")
    else:
        print(f"'{email1}' to NIEPRAWIDŁOWY adres e-mail. Spróbuj jeszcze raz.")


try:
    while menu_index != 3:

        if menu_index == 1:
            print("INFO: W Planie Numeracji Krajowej sieciom ruchomym zostały przydzielone następujące wyróżniki sieci (początek numeru): 50, 51, 53, 57, 60, 66, 69, 72, 73, 78, 79, 88")
            print()
            phone_number = input("Podaj numer telefonu (format 123456789 lub 123 456 789): ")
            print()
            phone_number_validator(phone_number)

        if menu_index == 2:
            print()
            email = input("Podaj adres e-maiil: ")
            print()
            email_validator(email)

        print()
        print("1. Walidacja numeru telefonu")
        print("2. Walidacja adresu e-mail")
        print("3. Wyjdź")
        print()
        menu_index = int(input("Wybierz dostępną opcję:"))

except ValueError:
    print("Wprowadzono błędną wartość. Aplikacja zostanie zamknięta.")
