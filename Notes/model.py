import view
import datetime
import os.path


def add_new_note():
    new_note = dict()
    new_note['Id'] = get_new_note_id()
    new_note['Header'] = view.get_user_input('note header')
    new_note['Text'] = view.get_user_input('note text')
    new_note['Time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if view.get_user_consent('save this note'):
        save_note(new_note)
        update_last_note_id(new_note['Id'])

def save_note(note):
    with open('Notes\\notebook.csv', 'a',encoding='utf-8') as file:
        file.write(f"{note['Id']};{note['Header']};{note['Text']};{note['Time']}\n")

def get_notes():
    if file_exists('Notes\\notebook.csv'):
        notes = dict()

        file = open('Notes\\notebook.csv', 'r',encoding='utf-8')
        file_text = file.readlines()
        file.close

        for i in range(0, len(file_text)):
            file_text[i] = file_text[i].replace('\n', '')
            temp = file_text[i].split(';')
            notes[int(temp[0])] = {}
            notes[int(temp[0])]['Header'] = temp[1]
            notes[int(temp[0])]['Text'] = temp[2]
            notes[int(temp[0])]['Time'] = temp[3]
        return notes
    return False

def edit_note(id):
    notes = get_notes()

    for key in notes:
        if key == id:
            notes[key]['Header'] = view.get_user_input('note header')
            notes[key]['Text'] = view.get_user_input('note text')
            notes[key]['Time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break

    save_notes(sort_notes(notes))

def delete_note(id):
    if view.get_user_consent(f'delete the note #{id}'):
        notes = get_notes()

        for key in notes:
            if key == id:
                notes.pop(key)
                break

        save_notes(notes)

def get_new_note_id():
    if file_exists('Notes\last_note_id.txt'):
        with open('Notes\last_note_id.txt', 'r',encoding='utf-8') as file:
            return int(file.read()) + 1
    else:
        return 1

def update_last_note_id(id):
    with open('Notes\last_note_id.txt', 'w',encoding='utf-8') as file:
        file.write(str(id))

def save_notes(notes):
    note = dict()
    with open('Notes\\notebook.csv', 'w',encoding='utf-8') as file:
        file.write('')

    for key in notes:
        note['Id'] = key
        note['Header'] = notes[key]['Header']
        note['Text'] = notes[key]['Text']
        note['Time'] = notes[key]['Time']
        save_note(note)

def note_id_check(id):
    notes = get_notes()

    if notes != False:
        if id in notes.keys():
            return True

    return False

def get_note_id():
    note_id = view.get_note_id('Enter note id you want to edit: ')

    if note_id_check(note_id):
        return note_id

    return '-1'

def file_exists(path):
    return os.path.isfile(path)

def sort_notes(notes):
    temp = dict()
    sorted_notes = dict()

    for key in notes:
        temp[key] = notes[key]['Time']

    sorted_temp = dict(sorted(temp.items(), key=lambda item:item[1]))

    for key in sorted_temp:
        sorted_notes[key] = {}
        sorted_notes[key]['Header'] = notes[key]['Header']
        sorted_notes[key]['Text'] = notes[key]['Text']
        sorted_notes[key]['Time'] = notes[key]['Time']

    return sorted_notes
