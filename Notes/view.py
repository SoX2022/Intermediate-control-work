import model

def show_notes():
    notes = model.get_notes()

    if notes == False:
        print("\033[31m{}\033[0m".format('There are no notes yet.'))
    else:
        
        for key in notes:
            header = notes[key]['Header']
            time = notes[key]['Time']
            print("\033[32m{}\033[0m".format(f'Id: {key}    |    {header}    |    {time}'))

    print()

def show_note(id):
    notes = model.get_notes()

    if notes == False:
        print("There are no notes yet.")
    else:
        if id not in notes.keys():
            print('There is no such note id.')
        else:
            for key in notes:
                if key == id:
                    header = notes[key]['Header']
                    time = notes[key]['Time']
                    print("\033[32m{}\033[0m".format(f'Id: {key}   |   {header}    |    {time}'))
                    print("\033[34m{}\033[0m".format(notes[key]['Text']))
                    break
    print()

def show_menu(menu_status):
    print('Choose an option:')
    if menu_status == 1:
        print('1. View notes')

    print('2. Add new note')

    if menu_status == 1:
        print('3. Show note')
        print('4. Edit note')
        print('5. Delete note')

    print('6. Exit')
    print()

def get_user_input(message):
    return input(f'Enter {message}: ')

def get_user_consent(message):
    while True:
        print("\033[36m{}\033[0m".format(f'Do you want to {message}?\nY/N '))
        result = input().lower()
        match result:
            case 'y':
                return True
            case 'n':
                return False
        print("\033[31m{}\033[0m".format('Illigal argument.\n'))

def get_user_answer(menu_status):
    match menu_status:
        case 0:
            answers = ['2', '6']
        case 1:
            answers = ['1', '2', '3', '4', '5', '6']

    user_input = input()

    while user_input not in answers:
        print("\033[31m{}\033[0m".format('Illigal argument.\n'))
        print()
        show_menu(menu_status)
        user_input = input()
    
    return user_input

def get_note_id(message):
    note_id = int(input(message))

    if model.note_id_check(note_id):
        return note_id
    
    print("\033[31m{}\033[0m".format('There is no such note id.'))
    print()
    return '-1'

