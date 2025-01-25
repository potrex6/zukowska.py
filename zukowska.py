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
        "Musimy dążyć do zrównoważonego rozwoju, dlatego",
        "Konieczne jest wprowadzenie sprawiedliwości społecznej, dlatego",
        "Chcemy społeczeństwa, w którym każdy jest równy, dlatego",
        "Prawa człowieka muszą być zawsze na pierwszym miejscu, dlatego",
        "Równość dla osób LGBTQ+ to nasz obowiązek, dlatego",
        "Związki jednopłciowe muszą mieć takie same prawa jak małżeństwa heteroseksualne, dlatego",
        "Aborcja to prawo każdej kobiety, dlatego",
        "Nie możemy ograniczać wyborów kobiet w kwestii aborcji, dlatego",
        "Prawa reprodukcyjne to prawa człowieka, dlatego",
        "Mazowsze graniczy z Białorusią, dlatego",
        "Mężczyzna może urodzić dziecko, dlatego",
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
        "walczymy o lepsze warunki pracy dla każdej osoby.",
        "chcemy uczciwego podziału bogactwa.",
        "zrównoważony rozwój i sprawiedliwość muszą stać się priorytetem.",
        "musimy zadbać o naszą planetę i przyszłe pokolenia.",
        "domagamy się zmiany w systemie edukacji na bardziej sprawiedliwy.",
        "musimy zagwarantować równość i prawa dla wszystkich, bez względu na orientację seksualną.",
        "równość w dostępie do usług zdrowotnych, w tym aborcji, to nasze zadanie.",
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
        "Każdy zasługuje na lepsze życie, dlatego",
        "Jesteśmy za systemem, który działa dla ludzi, a nie dla korporacji, dlatego",
        "Przyszłość, w której nikt nie zostanie pominięty, dlatego",
        "Musimy zmienić system, aby działał na rzecz każdego człowieka, dlatego",
        "W której każda kobieta ma pełne prawo do decydowania o swoim ciele, dlatego",
        "Każda osoba LGBTQ+ ma prawo do równości i akceptacji, dlatego",
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
        "społeczeństwo oparte na wzajemnym szacunku i solidarności.",
        "nasza przyszłość to sprawiedliwość i zrównoważony rozwój.",
        "równość dla wszystkich, bez względu na pochodzenie czy status.",
        "świat, w którym nikt nie jest zostawiony samemu sobie.",
        "każdy człowiek zasługuje na szansę na lepsze życie.",
        "wolność, równość i braterstwo muszą stać się rzeczywistością.",
        "prawa osób LGBTQ+ to integralna część praw człowieka.",
        "prawo do aborcji to kwestia wolności wyboru i szacunku dla kobiet.",
        "prawo do decydowania o swoim ciele to prawo każdej osoby.",
        "powinniśmy zacząć jeść robaki zamiast mięsa.",
    ],
]


def zukowska_random():
    answer = [random.choice(ZUKOWSKA[i]) for i in range(len(ZUKOWSKA))]
    return " ".join(answer)


if __name__ == "__main__":
    print(zukowska_random())
