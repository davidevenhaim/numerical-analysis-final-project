import random


def random_question(id1, id2, id3, id4):
    question_number = list()

    last_digit1 = int(id1) % 10
    last_digit2 = int(id2) % 10
    last_digit3 = int(id3) % 10
    last_digit4 = int(id4) % 10

    # part 1 - question 1
    question_number.append(random.choice([last_digit1, last_digit2, last_digit3, last_digit4]))
    if question_number[0] == 0:
        question_number[0] = 1

    # part 2 - question 2 & 3
    question_number.append(random.choice([random.randint(last_digit1 + 10, 18), last_digit2 + 10, last_digit3 + 10,
                                          last_digit4 + 10]))
    if question_number[1] > 18:
        question_number[1] = 18
    question_number.append(random.choice([last_digit1 + 10, last_digit2 + 10, last_digit3 + 10, last_digit4 + 10]))
    if question_number[2] > 18:
        question_number[2] = 18
    while question_number[1] == question_number[2]:
        question_number[2] = random.choice([last_digit1 + 10, last_digit2 + 10, last_digit3 + 10, last_digit4 + 10])
        if question_number[2] > 18:
            question_number[2] = 18

    # part 3 - question 4 & 5
    question_number.append(random.choice([random.randint(last_digit1 + 19, 30), last_digit2 + 19,
                                          random.randint(last_digit1 + 19, 30),last_digit4 + 19]))
    if question_number[3] > 30:
        question_number[3] = 30
    question_number.append(random.choice([last_digit1 + 19, last_digit2 + 19, last_digit3 + 19, last_digit4 + 19]))
    if question_number[4] > 30:
        question_number[4] = 30
    while question_number[3] == question_number[4]:
        question_number[4] = random.choice([last_digit1 + 19, last_digit2 + 19, last_digit3 + 19, last_digit4 + 19])
        if question_number[4] > 30:
            question_number = 30

    # part 4 - question 6
    question_number.append(random.choice([last_digit1 + 31, last_digit2 + 31, last_digit3 + 31, last_digit4 + 31]))
    if question_number[5] > 36:
        question_number[5] = 36

    return question_number


id_noa = 209507680
id_david = 208537019
id_adi = 316413780
id_asaf = 207809997


random_questions = random_question(id_noa, id_david, id_adi, id_asaf)

print(random_questions)