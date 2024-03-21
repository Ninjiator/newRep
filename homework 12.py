import os
import string

films_titles = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}

# Крок 2: Створення тек для кожного фільму та літер
def create_directories():
    for film in films_titles["results"]:
        film_title = film["title"]
        # Замінюємо неприпустимі символи у назві фільму на підкреслення
        valid_film_title = ''.join(c if c.isalnum() else '_' for c in film_title)
        film_directory = os.path.join("Harry Potter", valid_film_title)
        os.makedirs(film_directory, exist_ok=True)

        for letter in string.ascii_uppercase:
            letter_directory = os.path.join(film_directory, letter)
            os.makedirs(letter_directory, exist_ok=True)

# Крок 3: Створення списку нагород для кожного фільму
def create_awards_lists():
    for film in films_titles["results"]:
        if "awards" not in film:
            film["awards"] = []  # Якщо нагороди відсутні, створюємо порожній список
        sorted_awards_list = sorted(film["awards"], key=lambda x: x.get("award_name", ""))
        film["awards"] = sorted_awards_list

# Крок 5-6: Створення файлів з назвами нагород та запис номінацій
def create_award_files():
    for film in films_titles["results"]:
        film_title = film["title"]
        # Замінюємо неприпустимі символи у назві фільму на підкреслення
        valid_film_title = ''.join(c if c.isalnum() else '_' for c in film_title)
        for award in film["awards"]:
            award_name = award["award_name"]
            first_letter = award_name[0].upper()
            file_path = os.path.join("Harry Potter", valid_film_title, first_letter, f"{award_name}.txt")
            with open(file_path, "w") as file:
                for nomination in film["awards"]:
                    if nomination["award_name"] == award_name:
                        file.write(nomination["award"] + "\n")

# Виконання кроків
create_directories()
create_awards_lists()
create_award_files()
