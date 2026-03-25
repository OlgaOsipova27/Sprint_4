import pytest

from Sprint_4.main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    
    @pytest.mark.parametrize('name', 
[
    'Как выжить, если ваш кот — гений зла', #41 символ
    'Что делать, если ваш кот хочет вас убить', #54 символа
    '' #0 символов
])
    def test_test_add_new_book_add_invalid_symbols_in_name(self,name):

        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.books_genre) == 0


    def test_set_book_genre_valid_genre(self):
         collector = BooksCollector()
         
         collector.add_new_book('Тридцатилетняя женщина')
         collector.set_book_genre('Тридцатилетняя женщина', 'Детективы')

         assert collector.books_genre['Тридцатилетняя женщина'] == 'Детективы'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тридцатилетняя женщина')
        collector.set_book_genre('Тридцатилетняя женщина', 'Драмы')

        assert collector.books_genre['Тридцатилетняя женщина'] == ''
    
    def test_set_book_genre_missing_book_name(self):
        collector = BooksCollector()
       
        collector.set_book_genre('Тридцатилетняя женщина', 'Детективы')
        
        assert 'Тридцатилетняя женщина' not in collector.books_genre

    def test_get_book_genre_valid_name(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тридцатилетняя женщина')
        collector.add_new_book('Три мушкетера')
        
        collector.set_book_genre('Тридцатилетняя женщина', 'Детективы')
        collector.set_book_genre('Три мушкетера', 'Фантастика')

        assert collector.get_book_genre('Тридцатилетняя женщина') == 'Детективы'

    def test_get_books_with_specific_genre_valid_genre(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тридцатилетняя женщина')
        collector.add_new_book('Три мушкетера')
        
        collector.set_book_genre('Тридцатилетняя женщина', 'Детективы')
        collector.set_book_genre('Три мушкетера', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Три мушкетера']

    def test_get_books_for_children_horror_not_in_list(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тридцатилетняя женщина')
        collector.set_book_genre('Тридцатилетняя женщина', 'Ужасы')

        assert  'Тридцатилетняя женщина' not in collector.get_books_for_children() and 'Три мушкетера' not in collector.get_books_for_children()


    def test_add_book_in_favorites_add_book(self):

        collector = BooksCollector()
        
        collector.add_new_book('Тридцатилетняя женщина')
        collector.add_new_book('Три мушкетера')
        
        collector.set_book_genre('Тридцатилетняя женщина', 'Детективы')
        collector.set_book_genre('Три мушкетера', 'Фантастика')

        collector.add_book_in_favorites('Тридцатилетняя женщина')

        assert len(collector.favorites) == 1


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тридцатилетняя женщина')
        collector.add_new_book('Три мушкетера')
        
        collector.set_book_genre('Тридцатилетняя женщина', 'Детективы')

        collector.add_book_in_favorites('Тридцатилетняя женщина')
        collector.add_book_in_favorites('Три мушкетера')

        collector.delete_book_from_favorites('Три мушкетера')

        assert 'Три мушкетера' not in collector.favorites

    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        
        collector.add_new_book('Тридцатилетняя женщина')
        collector.add_new_book('Три мушкетера')
        
        collector.set_book_genre('Тридцатилетняя женщина', 'Детективы')

        collector.add_book_in_favorites('Тридцатилетняя женщина')
        collector.add_book_in_favorites('Три мушкетера')

        assert collector.get_list_of_favorites_books() == ['Тридцатилетняя женщина', 'Три мушкетера']
