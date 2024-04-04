#!/usr/bin/python3
"""
Validate UTF8 data
"""

def validUTF8(data):
    # Count of remaining continuation bytes required
    remaining = 0

    for byte in data:
        # If no continuation bytes required
        if remaining == 0:
            # Single byte character
            if byte >> 7 == 0:
                continue
            # Two-byte character
            elif byte >> 5 == 0b110:
                remaining = 1
            # Three-byte character
            elif byte >> 4 == 0b1110:
                remaining = 2
            # Four-byte character
            elif byte >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            # Check if the byte starts with 10
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    # If there are remaining continuation bytes required
    if remaining != 0:
        return False

    return True