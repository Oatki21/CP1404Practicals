import wikipedia
term = input("Enter a title or search phrase")
while term != "":
    try:
        print(wikipedia.page(term).title)
        print(wikipedia.page(term).summary)
        print(wikipedia.page(term).url)
        term = input("Enter a title or search phrase")
    except wikipedia.exceptions.DisambiguationError:
        print("There are multiple results. Please specify")
        print(wikipedia.search(term))
        term = input("Enter a title or search phrase")

