import re
from word2number import w2n

def evaluate_expression(expression):
    try:
        # Replace words with numbers
        words_to_numbers = {
            "plus": "+",
            "minus": "-",
            "times": "*",
            "multiplied by": "*",
            "divided by": "/",
            "over": "/"
        }
        
        # Convert words to symbols
        for word, symbol in words_to_numbers.items():
            expression = expression.replace(word, symbol)
        
        # Handle multi-word numbers
        def replace_multi_word_numbers(match):
            try:
                return str(w2n.word_to_num(match.group(0)))
            except ValueError:
                return match.group(0)
        
        expression = re.sub(r'\b(?:one|two|three|four|five|six|seven|eight|nine|ten|'
                            r'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|'
                            r'eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|'
                            r'eighty|ninety|hundred|thousand|million|billion|trillion)+\b(?: \b(?:one|two|three|four|five|six|seven|eight|nine|ten|'
                            r'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|'
                            r'eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|'
                            r'eighty|ninety|hundred|thousand|million|billion|trillion)+\b)*', 
                            replace_multi_word_numbers, expression)
        
        # Convert written numbers to digits
        words = expression.split()
        for i, word in enumerate(words):
            try:
                words[i] = str(w2n.word_to_num(word))
            except ValueError:
                pass
        expression = " ".join(words)
        
        # Evaluate the mathematical expression
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception as e:
        return f"Error! Invalid input: {e}"

def calculator():
    print("Welcome to the Enhanced Calculator App!")
    print("You can type equations using words (e.g., 'two plus two') or symbols (e.g., '2 + 2').")
    
    while True:
        expression = input("Enter your math equation: ")
        result = evaluate_expression(expression)
        print(f"The result is: {result}")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the Enhanced Calculator App!")
            break

if __name__ == "__main__":
    calculator()