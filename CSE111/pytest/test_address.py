from address import extract_city, extract_state, extract_zipcode
import pytest

# Test function for extract_city
def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("1234 Elm St, Boise, ID 83702") == "Boise"
    assert extract_city("987 Maple Ave, New York, NY 10001") == "New York"
    assert extract_city("456 Oak Rd, Chicago, IL 60616") == "Chicago"
    assert extract_city("789 Pine St, Los Angeles, CA 90001") == "Los Angeles"

# Test function for extract_state
def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("1234 Elm St, Boise, ID 83702") == "ID"
    assert extract_state("987 Maple Ave, New York, NY 10001") == "NY"
    assert extract_state("456 Oak Rd, Chicago, IL 60616") == "IL"
    assert extract_state("789 Pine St, Los Angeles, CA 90001") == "CA"

# Test function for extract_zipcode
def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("1234 Elm St, Boise, ID 83702") == "83702"
    assert extract_zipcode("987 Maple Ave, New York, NY 10001") == "10001"
    assert extract_zipcode("456 Oak Rd, Chicago, IL 60616") == "60616"
    assert extract_zipcode("789 Pine St, Los Angeles, CA 90001") == "90001"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
