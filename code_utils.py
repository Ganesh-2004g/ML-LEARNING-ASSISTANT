def code_prompt(topic, level="detailed"):
    """
    Creates prompt for Python code generation
    """
    return f"""
    Write a Python implementation for:
    Topic: {topic}

    Requirements:
    - Beginner friendly
    - Well commented
    - Uses standard libraries
    - Includes example usage
    - Explains dependencies

    Complexity level: {level}
    """
