# rejestrOsobowy
Laboratorium 1 - miniprojekt "Rejestr osobowy" w ramach zajęć "Programowanie zaawansowane"

## Opis
Program umożliwia tworzenie prostej bazy użytkowników, z możliwością dodawania nowych danych do kolekcji, modyfikowania ich lub usuwania, exportowanie/importowanie zestawu danych a także przeszukiwanie bazy po wskazanej frazie.

Aplikacja jest stworzona w modelu obiektowym dzięki czemu możliwe jest wygodne dodawanie nowych typów danych lub poleceń.

Rozwiązanie zostało zweryfikowane pod kątem poprawności PEP8 przy użyciu pylint.

## Setup
0. Sklonuj to repo
1. Zbuduj image:
   ```bash
   docker build -t rejestrOsobowy .
   ```
3. Uruchom container z image:
   ```bash
   docker run -it rejestrOsobowy
   ```

## Instrukcja
Po poprawnym zbudowaniu projektu w formie aplikacji terminalowej możliwe jest wykonywanie poleceń.

Lista dostępnych komend dostępna jest przy użyciu polecenia `help`

Polecenia nie posiadają dodatkowych argumentów - w przypadku gdy potrzebne jest sprecyzowanie argumentów dla danego polecenia terminal wyświetli formularz.

## Lista komend:
- `add` - Dodaje nowy rekord
- `edit` - Edytuje rekord po wskazaniu guid oraz danych do zmiany (należy wskazać guid oraz typ w formularzu)
- `exit` - Opuszcza program
- `help` - Wyswietla listę komend wraz z ich opisami
- `list` - Wyswietla zapisane dane w cache programu
- `load` - Importuje plik znajdujacy się w katalogu Import (należy wskazać nazwę w formularzu)
- `remove` - Usuwa rekord
- `save` - Eksportuje cache do pliku (należy wskazać nazwę w formularzu)
- `search` - Przeszukuje cache pod wskazaną frazą
