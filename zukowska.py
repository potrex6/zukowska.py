import random

ZUKOWSKA = [
    [
        "Każdy ma prawo do godności, dlatego",
        "Nie możemy pozwolić na łamanie praw człowieka, dlatego",
        "Społeczeństwo bez równości to społeczeństwo niesprawiedliwe, dlatego",
        "Kapitalizm nie rozwiąże problemów społecznych, dlatego",
        "Każdy ma prawo do dachu nad głową, dlatego",
        "Żyjemy w systemie, który uprzywilejowuje bogatych, dlatego",
        "Musimy walczyć z nierównościami ekonomicznymi, dlatego",
        "Solidarność międzyludzka to nasz obowiązek, dlatego",
        "Walka o prawa pracownicze to walka o lepszy świat, dlatego",
    ],
    [
        "musimy walczyć o prawa pracownicze.",
        "domagamy się równych szans dla wszystkich.",
        "wprowadzamy zmiany, które naprawdę służą ludziom.",
        "domagamy się progresywnego opodatkowania najbogatszych.",
        "wprowadzamy publiczne mieszkalnictwo dostępne dla każdego.",
        "chcemy zapewnić godne życie wszystkim, a nie tylko elitom.",
        "dążymy do skrócenia czasu pracy bez utraty wynagrodzenia.",
        "musimy zakończyć wyzysk na rynku pracy.",
        "rządy muszą inwestować w ludzi, nie w korporacje.",
    ],
    [
        "Bo Polska potrzebuje lewicowej wizji przyszłości, w której",
        "Dla przyszłych pokoleń, w których",
        "Żeby każdy człowiek mógł czuć, że",
        "Bo każda kobieta, każdy pracownik i każde dziecko musi wiedzieć, że",
        "Naszym celem jest świat, w którym",
        "Nie ma zgody na społeczeństwo, w którym",
        "Lewica walczy o przyszłość, gdzie",
        "Razem możemy zbudować system, w którym",
    ],
    [
        "sprawiedliwość wygrywa z uprzedzeniami.",
        "prawa jednostki są priorytetem.",
        "równość i solidarność stają się fundamentem społeczeństwa.",
        "sprawiedliwość społeczna zastępuje wyzysk.",
        "bogactwo jest dzielone równo, a nie kumulowane w rękach nielicznych.",
        "każdy ma dostęp do edukacji, zdrowia i godnego życia.",
        "ekonomia służy ludziom, a nie odwrotnie.",
        "równość i godność stają się prawem, a nie przywilejem.",
    ],
]


def zukowska_random():
    answer = [random.choice(ZUKOWSKA[i]) for i in range(len(ZUKOWSKA))]
    return " ".join(answer)


if __name__ == "__main__":
    print(zukowska_random())
