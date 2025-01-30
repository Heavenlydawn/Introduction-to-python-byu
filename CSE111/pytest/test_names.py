from names import make_full_name, extract_family_name, extract_given_name
import pytest

# Test function for make_full_name
def test_make_full_name():
    # Test various cases for full name creation
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Anna-Marie", "Smith") == "Smith; Anna-Marie"
    assert make_full_name("Mary Jane", "Doe") == "Doe; Mary Jane"
    assert make_full_name("A", "B") == "B; A"

# Test function for extract_family_name
def test_extract_family_name():
    # Test extracting the family name from full name
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Smith; Anna-Marie") == "Smith"
    assert extract_family_name("Doe; Mary Jane") == "Doe"
    assert extract_family_name("B; A") == "B"

# Test function for extract_given_name
def test_extract_given_name():
    # Test extracting the given name from full name
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Smith; Anna-Marie") == "Anna-Marie"
    assert extract_given_name("Doe; Mary Jane") == "Mary Jane"
    assert extract_given_name("B; A") == "A"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
