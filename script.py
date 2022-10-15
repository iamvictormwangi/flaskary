def generate_admin():
    choice = input("\nAdd admin feature (y,n) : ")

    if choice == 'y':
        print('Added admin feauture')
    elif choice == 'n':
        print('Disabled admin feauture')
    else:
        print('Chose either y or n.')
        generate_admin()


def chose_css_frmework():
    choice = input(
        "\nChose a css framework \n 1) Bootstrap \n 2) Tailwind \n 3) Bulma \n 4) Materialize \n 5) Chakra \n 6) Bulma \n 7) Limpio \n 8) None :")

    choice = int(choice)

    if choice == 1:
        print('Added Bootstrap')
    elif choice == 2:
        print('Added Tailwind')
    elif choice == 3:
        print('Added Bulma')
    elif choice == 4:
        print('Added Materialize')
    elif choice == 5:
        print('Added Chakra')
    elif choice == 6:
        print('Added Bulma')
    elif choice == 7:
        print('Added Limpio')
    elif choice == 8:
        print('None')
    else:
        print('Chose a valid option')


def chose_js_frmework():
    choice = input(
        "\nChose a javascript framework \n 1) React \n 2) Vue \n 3) AngularJS \n 4) Preact \n 5) Alpine \n 6) None :")

    choice = int(choice)

    if choice == 1:
        print('Added React')
    elif choice == 2:
        print('Added Vue')
    elif choice == 3:
        print('Added Angularjs')
    elif choice == 4:
        print('Added Preact')
    elif choice == 5:
        print('Added Alpine')
    elif choice == 6:
        print('None added')
    else:
        print('Chose a valid option')


chose_css_frmework()
chose_js_frmework()
