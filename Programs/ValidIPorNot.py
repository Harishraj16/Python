import re

def is_valid_ipv4(ip):
    # Define the regex pattern for a valid IPv4 address
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    
    # Check if the IP address matches the pattern
    if not pattern.match(ip):
        return False
    
    # Split the IP address into its components
    parts = ip.split('.')
    for part in parts:
        # Ensure each part is a number between 0 and 255
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
        # Check for leading zeros
        if len(part) > 1 and part[0] == '0':
            return False
    
    # If all checks pass, the IP address is valid
    return True

# Test cases
test_ips = [
    "192.168.1.1",
    "255.255.255.255",
    "0.0.0.0",
    "256.256.256.256",
    "192.168.1.01",
    "192.168.1",
    "192.168.1.abc"
]

for ip in test_ips:
    print(f"{ip} is valid IPv4 address: {is_valid_ipv4(ip)}")


'''
Here's what each part of the regular expression means:

^: Asserts the start of the string.
(\d{1,3}\.){3}:
\d{1,3}: Matches a sequence of 1 to 3 digits.
\.: Matches a literal dot (.). The backslash is used to escape the dot because a dot normally matches any character in regex.
{3}: The previous sequence (1 to 3 digits followed by a dot) is repeated exactly 3 times.
\d{1,3}: Matches a sequence of 1 to 3 digits (the last part of the IP address, which does not end with a dot).
$: Asserts the end of the string.
'''
