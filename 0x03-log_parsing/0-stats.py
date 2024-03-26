#!/usr/bin/env python3
import sys
from collections import defaultdict

"""Log parsing"""

def print_statistics(total_file_size, status_codes):
    """ log parsing first function"""
    print("File size:", total_file_size)
    for status_code in sorted(status_codes.keys()):
        print("{}: {}".format(status_code, status_codes[status_code]))

def parse_line(line):
    """ log parsing second function"""
    parts = line.strip().split()
    if len(parts) != 9:
        return None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not status_code.isdigit():
        return None, None
    return status_code, int(file_size)

def main():
    """ log parsing third function"""
    total_file_size = 0
    status_codes = defaultdict(int)
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_file_size += file_size
                status_codes[status_code] += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes)

if __name__ == "__main__":
    main()
