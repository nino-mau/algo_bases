from ex03_fonctions_algo.src.exercices import (
print_hello_world,
reverse_string,
to_uppercase,
count_substring,
list_length,
max_in_list,

    pgcd,
    fibonacci,
    crible_eratosthene,
    is_prime,
    is_palindrome,
    binary_search,
    gcd_recursive,
    fibonacci_recursive,
    is_palindrome_recursive,
    factorial_recursive
)

def test_print_hello_world():
    assert print_hello_world() == "Hello, World!"


def test_reverse_string():
    assert reverse_string("abcd") == "dcba"
    assert reverse_string("") == ""
    assert reverse_string("12345") == "54321"


def test_to_uppercase():
    assert to_uppercase("abcd") == "ABCD"
    assert to_uppercase("123") == "123"
    assert to_uppercase("") == ""


def test_count_substring():
    assert count_substring("hello world", "o") == 2
    assert count_substring("aaaaa", "aa") == 2
    assert count_substring("abcdef", "gh") == 0


def test_list_length():
    assert list_length([]) == 0
    assert list_length([1, 2, 3]) == 3
    assert list_length(["a", "b", "c", "d"]) == 4


def test_max_in_list():
    assert max_in_list([1, 2, 3, 4, 5]) == 5
    assert max_in_list([-1, -2, -3]) == -1
    assert max_in_list([42]) == 42


def test_pgcd():
    assert pgcd(0, 0) == 0
    assert pgcd(54, 24) == 6
    assert pgcd(1071, 462) == 21


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55


def test_crible():
    assert crible_eratosthene(1) == []
    assert crible_eratosthene(10) == [2, 3, 5, 7]
    assert crible_eratosthene(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(18) == False


def test_is_palindrome():
    assert is_palindrome("") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 5) == -1


def test_gcd_recursive():
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(1071, 462) == 21
    assert gcd_recursive(0, 0) == 0


def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(10) == 55


def test_is_palindrome_recursive():
    assert is_palindrome_recursive("") == True
    assert is_palindrome_recursive("radar") == True
    assert is_palindrome_recursive("hello") == False


def test_factorial_recursive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
