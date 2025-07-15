# 3
import json


def load_files(tests_file, values_file):
    with open(tests_file, 'r') as file:
        tests = json.load(file)

    with open(values_file, 'r') as file:
        values = json.load(file)
    return tests, values


tests, values = load_files('tests.json', 'values.json')

count_values = len(values['values'])


# Добавление по id всем по пути tests/
def id():
    count = []

    try:
        for i in range(0, 10000):
            count.append(len(tests['tests'][i]))
    except IndexError:
        pass

    for i in range(len(count)):
        try:
            for k in range(count_values):
                if tests['tests'][i]['id'] == values['values'][k]['id']:
                    tests['tests'][i]['value'] = values['values'][k]['value']
        except KeyError:
            continue

    return count


# Добавление по id всем по пути tests/values
def id1():
    count = []

    try:
        for i in range(0, 100):
            try:
                for k in range(0, 100):
                    count.append(len(tests['tests'][i]['values'][k]))
            except KeyError:
                continue
    except IndexError:
        pass

    for i in range(len(id())):
        try:
            for k in range(count_values):
                try:
                    for n in range(len(count)):
                        if tests['tests'][i]['values'][n]['id'] == values['values'][k]['id']:
                            tests['tests'][i]['values'][n]['value'] = values['values'][k]['value']
                except IndexError:
                    pass
        except KeyError:
            continue

    return count


# Добавление по id всем по пути tests/values/values
def id2():
    count = []

    try:
        for i in range(0, 100):
            try:
                for k in range(0, 100):
                    for n in range(0, 100):
                        count.append(len(tests['tests'][i]['values'][k]['values'][n]))
            except KeyError:
                continue
    except IndexError:
        pass

    for i in range(len(id())):
        try:
            for k in range(count_values):
                for n in range(len(id1())):
                    try:
                        for m in range(len(count)):
                            if tests['tests'][i]['values'][n]['values'][m]['id'] == values['values'][k]['id']:
                                tests['tests'][i]['values'][n]['values'][m]['value'] = values['values'][k]['value']
                    except IndexError:
                        pass
        except KeyError:
            continue

    return count


# Добавление по id всем по пути tests/values/values/values
def id3():
    count = []

    try:
        for i in range(0, 100):
            try:
                for k in range(0, 100):
                    for n in range(0, 100):
                        for m in range(0, 100):
                            count.append(len(tests['tests'][i]['values'][k]['values'][n]['values'][m]))
            except KeyError:
                continue
    except IndexError:
        pass

    for i in range(len(id())):
        try:
            for k in range(count_values):
                for n in range(len(id1())):
                    for m in range(len(id2())):
                        try:
                            for t in range(len(count)):
                                if tests['tests'][i]['values'][n]['values'][m]['values'][t]['id'] == \
                                        values['values'][k]['id']:
                                    tests['tests'][i]['values'][n]['values'][m]['values'][t]['value'] = \
                                    values['values'][k]['value']
                        except IndexError:
                            pass
        except KeyError:
            continue

    return count


id()
id1()
id2()
id3()

# Запись результатов в report.json
with open('report.json', 'w', encoding='utf-8') as file:
    json.dump(tests, file, ensure_ascii=False, indent=2)
