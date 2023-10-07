def circle_svg(text: str = ""):
    """
    Returns a string containing a SVG code to create a circle with an optional
    text on its center.
    """
    return """
      <circle cx="49" cy="49" r="35" fill="#303F9F" />
      <text x="50" y="50" font-size="16" text-anchor="middle" fill="white">
        {}
      </text>
    """.format(text)


def square_svg(color="#fff", arrow_direction: str = "", text: str = "", use_circle: bool = False) -> str:
    """
    Returns a string containing a SVG code to create a square with an optional
    arrow or circle drawn on its center.
    """
    points = ""
    if arrow_direction == "left":
        points = "25,50 75,25 75,75"
    elif arrow_direction == "right":
        points = "25,25 25,75 75,50"
    elif arrow_direction == "up":
        points = "50,25 25,75 75,75"
    elif arrow_direction == "down":
        points = "25,25 75,25 50,75"

    if use_circle:
        return f"""
            <rect width='100' height='100' fill='{color}' />
            {circle_svg(text)}
        """
    if arrow_direction == "":
        return f"""
            <rect width='100' height='100' fill='{color}' />
        """
    return f"""
        <rect width='100' height='100' fill='{color}' />
        <polygon points="{points}" fill="#303F9F" />
        <text x="50" y="20" font-size="16" text-anchor="middle" fill="#303F9F">
            {text}
        </text>
        """
