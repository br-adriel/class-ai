from grid import Grid


def circle_svg(text: str = ""):
    """
    Returns a string containing a SVG code to crate a circle with an optional
    text on its center.

    :param text: Text shown in the circle center (optional).
    :type text: str

    :return: A string containing a SVG code to draw a circle.
    :rtype: str
    """
    return """
    <svg height="100" width="100">
      <circle cx="49" cy="49" r="35" fill="#0000ff" />
      <text x="50" y="50" font-size="16" text-anchor="middle" fill="white">
        {}
      </text>
    </svg>
    """.format(text)

class HTMLGrid:
    """
    HTMLGrid class for generating an HTML grid visualization.

    Attributes:
        css (str): CSS styles for the grid.

    Args:
        grid (Grid | None): A Grid object to initialize from (optional).
        dimension (tuple[int, int]): The dimensions of the grid (default: (0, 0)).
        start (int | None): The starting position (optional, default: None).
        goal (int | None): The goal position (optional, default: None).
        path (list[int]): List of positions representing the path (default: []).
        obstacles (list[int]): List of positions representing obstacles (default: []).
    """

    css = """
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }

    .square {
        background: #fff;
        width: 100px;
        min-width: 100px;
        height: 100px;
        min-height: 100px;
        border: 1px solid black;
        display: inline-block;
        position: relative;
    }

    .square span {
        position: absolute;
        top: 2px;
        left: 2px;
    }

    .blocked {
        background: #D32F2F;
        color: #fff;
    }

    .used {
        background: #00E676;
    }

    .line {
        display: flex;
        width: auto;
    }
    """.strip()
    
    def __init__(
            self, *,
            grid: Grid | None = None,
            dimension: tuple[int, int] = (0, 0),
            start: int | None = None,
            goal: int | None = None,
            path: list[int] = [],
            obstacles: list[int] = []
            ):
        if grid is not None:
            self.dimension = grid.dimension
            self.obstacles = grid.obstacles
        else:
            self.dimension = dimension
            self.obstacles = obstacles

        self.start = 0 if start is None else start
        self.goal = self.dimension[0] * self.dimension[1] -1 if goal is None else goal
        
        self.path = path

        self.html_start = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>HTML Grid</title>
                <style>{}</style>
            </head>
            <body>
        """.format(self.css).strip()
        self.html_end = "</body></html>"
        
        
    def generateFile(self, filename: str = "grid"):
        """
        Generates an HTML file with a grid visualization.

        This method generates an HTML file containing a grid based on the class's
        attributes. The grid includes squares representing positions, and it may
        highlight obstacles, the start, and the goal positions.

        :param filename: The name of the HTML file to be generated (default: 'grid').
        :type filename: str

        :return: None
        :rtype: None
        """
        html_content = "<main>"
        for i in range(self.dimension[1]):
            html_content += "<div class='line'>"
            for j in range(self.dimension[0]):
                position = i * self.dimension[1] + j

                html_content += "<div class='square"

                if position in self.obstacles:
                    html_content += " blocked "
                elif position in self.path:
                    html_content += " used "

                if position == self.start:
                    html_content += f"'><span>{i}-{j}</span>{circle_svg('START')}</div>"
                elif position == self.goal:
                    html_content += f"'><span>{i}-{j}</span>{circle_svg('END')}</div>"
                else:
                    html_content += f"'><span>{i}-{j}</span></div>"
            html_content += "</div>"
        html_content += "</main>"


        # saving the file
        with open(filename + '.html', 'w') as html_file:
            html_file.write(self.html_start + html_content + self.html_end)
