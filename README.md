# sprint_4

Реализованы тесты: 
- test_test_add_new_book_add_invalid_symbols_in_name - проверка добавления книги с некорректной длиной названия (пустая строка, 41 символ, 54 символа)
- test_set_book_genre_valid_genre - проверка добавления валидного жанра 
- test_set_book_genre_invalid_genre - проверка добавления невалидного (отсутствующего в списке) жанра 
- test_set_book_genre_missing_book_name - проверка добавления жанра для книги названия которой нет в списке 
- test_get_book_genre_valid_name - проверка получения жанра книги по названию, с валидным названием 
- test_get_books_with_specific_genre_valid_genre - проверка получения книг по жанру, который есть в списке имеющихся книг
- test_get_books_for_children_horror_not_in_list - проверка, что книга с жанром Ужасы не будет добавлена в список для детей
- test_add_book_in_favorites_add_book - проверка добавления книги с существующим именем ранее не добавленной в избранное
- test_delete_book_from_favorites_delete_book - проверка удаления книги из избранного
- test_get_list_of_favorites_books_get_list - проверка получения списка избранного 
