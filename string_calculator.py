import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = [',', '\n']
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers[2:].split('\n', 1)
            custom_delimiters = re.findall(r'\[([^]]+)\]', delimiter_section)
            delimiters.extend(custom_delimiters)

        # Create a single regex pattern to split by multiple delimiters
        regex_pattern = '|'.join(map(re.escape, delimiters))
        num_list = re.split(regex_pattern, numbers)

        # Filter out numbers greater than 1000
        num_list = [int(num) for num in num_list if int(num) <= 1000]

        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

        return sum(num_list)

