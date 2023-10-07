def circle_svg(text: str = "", x: int = 0, y: int = 0) -> str:
    """
    Returns a string containing a SVG code to create a circle with an optional
    text on its center.
    """
    svg = f"<circle cx='{x + 49}' cy='{y + 49}' r='35' fill='#303F9F' />"
    svg += text_svg(text=text, x=x + 50, y=y+50)
    return svg


def text_svg(
    text: str = "",
    color: str = "#fff",
    x: int = 0,
    y: int = 0
) -> str:
    """
    Returns a string containing a SVG code to create a centered text
    """
    svg = f"<text x='{x}' y='{y}' font-size='16' text-anchor='middle' fill='{color}'>"
    svg += text + "</text>"
    return svg


def square_svg(
    color="#fff",
    arrow_direction: str = "",
    text: str = "",
    use_circle: bool = False,
    x: int = 0,
    y: int = 0,
    border: bool = False,
) -> str:
    """
    Returns a string containing a SVG code to create a square with an optional
    arrow or circle drawn on its center.
    """
    points = ""
    if arrow_direction == "left":
        points = f"{25+x},{50+y} {75+x},{25+y} {75+x},{75+y}"
    elif arrow_direction == "right":
        points = f"{25+x},{25+y} {25+x},{75+y} {75+x},{50+y}"
    elif arrow_direction == "up":
        points = f"{50+x},{25+y} {25+x},{75+y} {75+x},{75+y}"
    elif arrow_direction == "down":
        points = f"{25+x},{25+y} {75+x},{25+y} {50+x},{75+y}"

    if use_circle:
        svg = f"<rect width='100' height='100' fill='{color}' x='{x}' y='{y}' "
        svg += '' if not border else "stroke='black' stroke-width='1' "
        svg += '/>' + circle_svg(text, x=x, y=y)
        return svg
    if arrow_direction == "":
        svg = f"<rect width='100' height='100' fill='{color}' x='{x}' y='{y}' "
        svg += '' if not border else "stroke='black' stroke-width='1' "
        svg += "/>"
        return svg

    svg = f"<rect width='100' height='100' fill='{color}' x='{x}' y='{y}' "
    svg += '' if not border else "stroke='black' stroke-width='1' "
    svg += f"/><polygon points='{points}' fill='#303F9F' />"
    svg += text_svg(text, '#303f9f', x+50, y+20)
    return svg
