import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# capitalize


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),                    # первая строчная → заглавная
    ("hello Lena", "Hello lena"),            # заглавная у первого у второго
    ("labliTeh", "Labliteh"),                # наличие заглавной в теле слова
    ("Test", "Test"),                  # строка уже с заглавной — не меняется
    ("123", "123"),                    # числа как строка — регистр не меняется
    ("06 october 2026", "06 october 2026"),  # строка с пробелами и цифрами
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("SKYPRO", "Skypro"),   # все заглавные в слове
    ("", ""),               # пустая строка — не падает
    ("   ", "   "),         # строка с пробелами
    ("27cde", "27cde"),     # цифра в начале — регистр не меняется
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),                 # три пробела в начале
    (" hello mam", "hello mam"),             # пробелы + пробел внутри
    (" python", "python"),                   # один пробел в начале
    ("Test", "Test"),                        # не пустая строка без пробелов
    ("06 october 2026", "06 october 2026"),  # строка с пробелами внутри
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),    # пробелов нет — не меняется
    ("", ""),                # пустая строка — цикл не запускается
    ("   ", ""),             # только пробелы — все удаляются
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# contains


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),    # символ в начале
    ("SkyPro", "y", True),    # символ в середине
    ("SkyPro", "Pro", True),  # подстрока, а не один символ
    ("Тест", "Т", True),      # кириллица
    ("567", "6", True),       # цифра в строке
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "L", False),         # символа нет вообще
    ("SkyPro", "s", False),         # другой регистр — не совпадает
    ("", "P", False),               # пустая строка — не падает
    (" ", "S", False),              # строка с пробелом
    ("123", "4", False),            # цифры нет
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# delete_symbol


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "y", "SkPro"),           # удаление одного символа
    ("SkyPro", "Pro", "Sky"),           # удаление подстроки
    ("SkyProSky", "S", "kyProky"),      # несколько вхождений — удаляются все
    ("Тест", "т", "Тес"),               # удаление при тексте на кириллице
    ("123", "2", "13"),                 # удаление цифры в строке
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "L", "SkyPro"),      # символа нет — не меняется
    ("", "S", ""),                  # пустая строка — не падает
    ("SkyPro", "", "SkyPro"),       # пустой символ — replace ничего не удалит
    (" ", "S", " "),                # строка с пробелом
    ("689", "5", "689"),            # цифры нет
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
