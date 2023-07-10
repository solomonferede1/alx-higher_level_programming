#!/usr/bin/python3
"""
101-stats module
"""


import sys
from collections import defaultdict

def compute_metrics():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0
    
    try:
        for line in sys.stdin:
            if line_count % 10 == 0 and line_count > 0:
                print_statistics(total_size, status_codes)
            
            parts = line.split()
            
            if len(parts) < 8:
                continue
            
            size = int(parts[6])
            total_size += size
            
            status_code = parts[8]
            status_codes[status_code] += 1
            
            line_count += 1
    
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

def print_statistics(total_size, status_codes):
    print("Total file size:", total_size)
    
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

compute_metrics()