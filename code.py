import csv

all_words = {}
sections = ["esm", "famil", "keshvar", "rang", "ashia", "ghaza"]
for section in sections:
    all_words[section] = []


def normalize(s):
    if not s:
        return ""
    return s.replace(" ", "")


def ready_up():
    csvdata = open("esm_famil_data.csv")
    reader = csv.reader(csvdata)
    next(reader)
    for row in reader:
        all_words["esm"].append(normalize(row[0]))
        all_words["famil"].append(normalize(row[1]))
        all_words["keshvar"].append(normalize(row[2]))
        all_words["rang"].append(normalize(row[3]))
        all_words["ashia"].append(normalize(row[4]))
        all_words["ghaza"].append(normalize(row[5]))


participants = []


def add_participant(participant, answers):
    for section in sections:
        answers[section] = normalize(answers[section])
    participants.append({"name": participant, "answers": answers})


def calculate_all():
    global score
    scores = {}
    for participant in participants:
        this_name = participant["name"]
        this_answers = participant["answers"]
        scores[this_name] = 0
        for section in sections:
            this_answer = normalize(this_answers.get(section, False))
            if not this_answer or this_answer not in all_words[section]:
                score = 0
            else:
                duplicate = False
                all_answered = True
                for other in participants:
                    if this_name == other["name"]:
                        continue
                    other_answer = normalize(other["answers"][section])
                    if other_answer == this_answer:
                        duplicate = True
                    if not normalize(other_answer):
                        all_answered = False
                if all_answered and duplicate:
                    score = 5
                if not all_answered and duplicate:
                    score = 10
                if all_answered and not duplicate:
                    score = 10
                if not all_answered and not duplicate:
                    score = 15
            scores[this_name] += score

    return scores