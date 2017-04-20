from Prac07.programminglanguage import ProgrammingLanguage


def main():
    language_list = []
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    language_list = [ruby,python,vb]
    print(language_list)
    print([str(language) for language in language_list])



    print("The dynamically typed languages are:")
    print([language.name for language in language_list if language.is_dynamic()])


main()
