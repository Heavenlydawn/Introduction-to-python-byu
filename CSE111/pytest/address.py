def extract_city(address):
    """Extract and return the city from a U.S. mailing address."""

    # Extract city 
    city = address.split(",")[1].strip()
    return city



def extract_state(address):
    """Extract and return the state from a U.S. mailing address."""

    # Extract state
    state = address.split(",")[2].strip().split(" ")[0]
    return state




def extract_zipcode(address):
    """Extract and return the zipcode from a U.S. mailing address."""

    # Extract the zipcode 
    zipcode = address.split(" ")[-1].strip()
    return zipcode