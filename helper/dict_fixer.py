import re

with open('assets/raw_dict.txt', 'r') as file:
    lines = file.readlines()

# Remove lines consisting of spaces
cleaned_lines = [
                    line for line in lines 
                        if not re.match(r'^\s*$', line)
                ]

with open('assets/cleaned_dict.txt', 'w') as file:
    file.writelines(cleaned_lines)

total_lines = len(lines)
cleaned_lines_count = len(cleaned_lines)
removed_lines_count = total_lines - cleaned_lines_count

print(f"Total lines: {total_lines}")
print(f"Cleaned lines: {cleaned_lines_count}")
print(f"Removed lines: {removed_lines_count}")