"""A simple command-line calculator."""


def calculate(first_number: float, operator: str, second_number: float) -> float:
    """Return the result of applying operator to two numbers."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError(f"Unsupported operator: {operator}")


def main() -> None:
    """Run an interactive calculator session."""
    print("Simple Calculator")
    print("Supported operators: +, -, *, /")

    first_number = float(input("Enter the first number: "))
    operator = input("Enter operator (+, -, *, /): ").strip()
    second_number = float(input("Enter the second number: "))

    result = calculate(first_number, operator, second_number)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
