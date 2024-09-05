#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    number_bytes = 0

    mask_1 = 1 << 7  # 10000000
    mask_2 = 1 << 6  # 01000000

    for i in data:
        mask_byte = 1 << 7  # 10000000, used to count the leading 1s

        if number_bytes == 0:
            # Count the number of leading 1s to determine byte length
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            # If the byte starts with 0, it's a 1-byte character (ASCII)
            if number_bytes == 0:
                continue

            # UTF-8 is only valid for 2 to 4 bytes
            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Ensure the byte is a continuation byte (starts with '10')
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    # If there are leftover expected bytes, return False
    return number_bytes == 0
