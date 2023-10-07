from typing import Union
from utils.svg import circle_svg, square_svg

USAGE = """\
Create an HTML description of a grid and a solution path.

{} <method> <graph>
  <method> - a: A-STAR (heuristic: Euclidean distance), b: BFS, d: DFS.
  <graph> - The graph description from a TGF file.\
"""


class HTMLGrid:
    """
    HTMLGrid class for generating an HTML grid visualization.
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
        self,
        dimension: tuple[int, int] = (0, 0),
        start: Union[int, None] = None,
        goal: Union[int, None] = None,
        path: list[int] = [],
        obstacles: list[int] = []
    ):

        self.dimension = dimension
        self.obstacles = obstacles
        self.start = 1 if start is None else start
        self.goal = self.dimension[0] * \
            self.dimension[1] if goal is None else goal

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

    def generate_file(self, filename: str = "grid"):
        """
        Generates an HTML file with a grid visualization.
        """
        html_content = "<main>"
        for i in range(1, self.dimension[1] + 1):
            # add div that represent a line
            html_content += "<div class='line'>"

            for j in range(1, self.dimension[0] + 1):
                # position of the current cell
                position = (i - 1) * self.dimension[1] + j
                shape_text = 'START' if position == self.start else ''

                # start creation of cell div
                html_content += "<div class='square'>"

                # add style classes according to cell role
                if position in self.obstacles:
                    html_content += f"{square_svg('#D32F2F')}"
                elif position in self.path:
                    # check if it's the end of the path
                    index = self.path.index(position)
                    if index - 1 >= 0:  # decrease index because path is ordered backwards
                        x1 = i
                        y1 = j
                        y2 = ((self.path[index-1] - 1) % self.dimension[0]) + 1
                        x2 = ((self.path[index-1] - 1) //
                              self.dimension[1]) + 1

                        # calculates arrow direction
                        direction = ''
                        if x1 > x2:
                            direction = 'up'
                        elif x1 < x2:
                            direction = 'down'
                        elif y1 > y2:
                            direction = 'left'
                        else:
                            direction = 'right'
                        html_content += square_svg(arrow_direction=direction,
                                                   color='#00E676',
                                                   text=shape_text)

                # add svg circle marking start and finish cells
                if position == self.goal:
                    html_content += f"<span>{i}-{j}</span>{square_svg(color='#00E676', text='END', use_circle=True)}</div>"
                else:
                    html_content += f"<span>{i}-{j}</span></div>"

            # close cell div
            html_content += "</div>"
        html_content += "</main>"

        # saving the file
        with open(filename + '.html', 'w') as html_file:
            html_file.write(self.html_start + html_content + self.html_end)


if __name__ == "__main__":
    """
    """
    from utils.path import path_dict_to_list
    import graph
    import sys
    import tgf

    if len(sys.argv) > 2:
        t = tgf.TGF(sys.argv[2])
        g = graph.Graph()
        t.read(g)
        ans = g.search(g.nodes[0], g.nodes[-1], graph.METHOD[sys.argv[1]])

        o = list(range(1, t.dimension[0] * t.dimension[1] + 1))
        for n in g.nodes:
            if int(n) in o:
                o.remove(int(n))

        hg = HTMLGrid(t.dimension,
                      path=path_dict_to_list(ans),
                      obstacles=o)
        hg.generate_file("grid-" + sys.argv[1])
    else:
        print(USAGE.format(sys.argv[0]))
