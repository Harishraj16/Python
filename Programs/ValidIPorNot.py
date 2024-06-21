import re

def is_valid_ipv4(ip):
    # Define the regex pattern for a valid IPv4 address
    # ^         : Start of the string
    # (\d{1,3}\.): 1 to 3 digits followed by a dot, repeated 3 times
    # \d{1,3}   : 1 to 3 digits (final part of the IP address)
    # $         : End of the string
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    
    # Check if the IP address matches the pattern
    if not pattern.match(ip):
        return False
    
    # Split the IP address into its four parts
    parts = ip.split('.')
    
    # Validate each part
    for part in parts:
        # Ensure the part is a number and in the range 0-255
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
        # Check for leading zeros (e.g., "01" is not valid)
        if len(part) > 1 and part[0] == '0':
            return False
    
    # If all parts are valid, return True
    return True

# Test cases to verify the function
test_ips = [
    "192.168.1.1",        # Valid IP
    "255.255.255.255",    # Valid IP
    "0.0.0.0",            # Valid IP
    "256.256.256.256",    # Invalid IP: parts out of range
    "192.168.1.01",       # Invalid IP: leading zero
    "192.168.1",          # Invalid IP: not enough parts
    "192.168.1.abc"       # Invalid IP: contains non-numeric characters
]

# Test the function with the test cases
for ip in test_ips:
    print(f"{ip} is valid IPv4 address: {is_valid_ipv4(ip)}")
