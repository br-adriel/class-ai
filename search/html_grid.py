from typing import Union

USAGE = """\
Create an HTML description of a grid and a solution path.

{} <method> <graph>
  <method> - a: A-STAR (heuristic: Euclidean distance), b: BFS, d: DFS.
  <graph> - The graph description from a TGF file.\
"""

def circle_svg(text: str = ""):
    """
    Returns a string containing a SVG code to create a circle with an optional
    text on its center.
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
        self.goal = self.dimension[0] * self.dimension[1] if goal is None else goal
        
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
        for i in range(1, self.dimension[1] +1):
            # add div that represent a line
            html_content += "<div class='line'>"

            for j in range(1, self.dimension[0] +1):
                # position of the current cell
                position = (i -1) * self.dimension[1] + j

                # start creation of cell div
                html_content += "<div class='square"

                # add style classes according to cell role
                if position in self.obstacles:
                    html_content += " blocked "
                elif position in self.path:
                    html_content += " used "

                # add svg circle marking start and finish cells
                if position == self.start:
                    html_content += f"'><span>{i}-{j}</span>{circle_svg('START')}</div>"
                elif position == self.goal:
                    html_content += f"'><span>{i}-{j}</span>{circle_svg('END')}</div>"
                else:
                    html_content += f"'><span>{i}-{j}</span></div>"
            
            # close cell div
            html_content += "</div>"
        html_content += "</main>"

        # saving the file
        with open(filename + '.html', 'w') as html_file:
            html_file.write(self.html_start + html_content + self.html_end)

if __name__ == "__main__":
    """
    """
    import sys
    import tgf
    import graph
    import utils

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
                      path = utils.path_dict_to_list(ans),
                      obstacles = o)
        hg.generate_file("grid-" + sys.argv[1])
    else:
        print(USAGE.format(sys.argv[0]))
