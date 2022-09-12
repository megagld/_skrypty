
def usun_pliki_tymczasowe(filenames):
    print('usun_pliki_tymczasowe')
    # print(filenames)
    input()

def foo3(filenames):
    print('foo3')
    print(filenames)
    input()


if __name__ == '__main__':
    from context_menu import menus
    
    # # usuń stare menu - do przerobienia
    # menus.removeMenu('pomoc', type='DIRECTORY_BACKGROUND')

    # dodaj nowe menu
    cm = menus.ContextMenu('pomoc', type='DIRECTORY_BACKGROUND')
    cm.add_items([
        menus.ContextCommand('Foo One666', command='echo hello > example.txt'),
        menus.ContextCommand('usun_pliki_tymczasowe.py', python=usun_pliki_tymczasowe)
    ])
    cm.compile()