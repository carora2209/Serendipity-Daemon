from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('86b5b0e76efdea155289fa8a45d1ece2')

    forms = jotformAPIClient.get_forms()

    for form in forms:
    	print(form["title"])

if __name__ == "__main__":
    main()
