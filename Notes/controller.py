import view
import model

def start ():
    menu_status = 0
    stop = False

    while not stop:
        if model.file_exists('Notes\\notebook.csv'):
            menu_status = 1

        view.show_menu(menu_status)
        user_choice = view.get_user_answer(menu_status)

        match user_choice:
            case '1':
                view.show_notes()
            case '2':
                model.add_new_note()
            case '3':
                note_id = view.get_note_id('Enter note id you want to look at: ')
                if note_id != '-1':
                    view.show_note(note_id)
            case '4':
                note_id = view.get_note_id('Enter note id you want to edit: ')
                if note_id != '-1':
                    model.edit_note(note_id)
            case '5':
                note_id = view.get_note_id('Enter note id you want to delete: ')
                if note_id != '-1':
                    model.delete_note(note_id)
            case '6':
                stop = True





