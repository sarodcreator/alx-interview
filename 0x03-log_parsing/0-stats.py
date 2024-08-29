#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

# Store the count of all status codes in a dictionary
status_codes_dict = {
    '200': 0, '301': 0, '400': 0, '401': 0, 
    '403': 0, '404': 0, '405': 0, '500': 0
}

total_size = 0
count = 0  # Keep count of the number of lines

def print_stats():
    """Print the accumulated metrics."""
    print('File size: {}'.format(total_size))
    for key in sorted(status_codes_dict.keys()):
        if status_codes_dict[key] != 0:
            print('{}: {}'.format(key, status_codes_dict[key]))

try:
    for line in sys.stdin:
        try:
            line_list = line.split(" ")
            if len(line_list) > 4:
                status_code = line_list[-2]
                file_size = int(line_list[-1])

                if status_code in status_codes_dict:
                    status_codes_dict[status_code] += 1

                total_size += file_size
                count += 1

                if count == 10:
                    print_stats()
                    count = 0  # Reset count after printing

        except (IndexError, ValueError):
            # Ignore lines that don't have the correct format
            continue

except KeyboardInterrupt:
    print_stats()
    raise

finally:
    print_stats()

