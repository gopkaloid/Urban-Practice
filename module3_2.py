def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not any(domain in recipient for domain in ("com", "ru", "net")) or \
            not any(domain in sender for domain in ("com", "ru", "net")) or \
            '@' not in recipient or '@' not in sender:
        print("Невозможно отправить письмо с адреса <%s> на адрес <%s>" % (sender, recipient))
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса <%s> на адрес <%s>" % (sender, recipient))
        return

    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <%s> на адрес <%s>" % (sender, recipient))


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')