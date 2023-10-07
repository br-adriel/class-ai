from typing import Union
from utils.svg import square_svg, text_svg


USAGE = """\
Create an SVG description of a grid and a solution path.

{} <method> <graph>
  <method> - a: A-STAR (heuristic: Euclidean distance), b: BFS, d: DFS.
  <graph> - The graph description from a TGF file.\
"""


class SVGGrid:
    """
    Class for generating an SVG grid visualization.
    """

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

    def generate_file(self, filename: str = "grid"):
        """
        Generates an SVG file with a grid visualization.
        """
        svg_content = f"<svg width='{100 * self.dimension[0]}' "
        svg_content += f"height='{100 * self.dimension[1]}' "
        svg_content += "xmlns='http://www.w3.org/2000/svg'>"

        for i in range(1, self.dimension[1] + 1):
            for j in range(1, self.dimension[0] + 1):
                # position of the current cell
                position = (i - 1) * self.dimension[1] + j
                shape_text = 'START' if position == self.start else ''

                svg_x = 100 * j - 100
                svg_y = 100 * i - 100

                # styles cell according to its role
                if position in self.obstacles:
                    svg_content += square_svg(border=True,
                                              color='#D32F2F', x=svg_x, y=svg_y)
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
                        svg_content += square_svg(border=True,
                                                  arrow_direction=direction,
                                                  color='#00E676',
                                                  text=shape_text,
                                                  x=svg_x,
                                                  y=svg_y)
                else:
                    svg_content += square_svg(border=True,
                                              x=svg_x,
                                              y=svg_y)

                # add svg circle marking start and finish cells
                if position == self.goal:
                    svg_content += square_svg(border=True,
                                              color='#00E676',
                                              text='END',
                                              use_circle=True,
                                              x=svg_x,
                                              y=svg_y)

                svg_content += f"<text x='{svg_x + 2}' y='{svg_y+16}' font-size='16' fill='#000'>{i}-{j}</text>"

        # saving the file
        with open(filename + '.svg', 'w') as svg_File:
            svg_File.write(svg_content + "</svg>")


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

        hg = SVGGrid(t.dimension,
                     path=path_dict_to_list(ans),
                     obstacles=o)
        hg.generate_file("grid-" + sys.argv[1])
    else:
        print(USAGE.format(sys.argv[0]))
