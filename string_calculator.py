class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split('\n', 1)
            numbers = numbers.replace(delimiter, ',')
        numbers = numbers.replace('\n', ',')
        num_list = numbers.split(',')
        
        negatives = [int(num) for num in num_list if int(num) < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
        
        return sum(int(num) for num in num_list)

