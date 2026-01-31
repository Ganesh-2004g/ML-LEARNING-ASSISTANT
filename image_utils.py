def generate_image_prompt(topic):
    """
    Creates a structured prompt for AI image generation
    """
    prompt = f"""
    Create a clean educational diagram for:
    Topic: {topic}
    Style: Minimal, labeled, technical
    Use case: Machine Learning education
    """
    return prompt
