from grid import Grid

USAGE = """\
Create a TGF descrition of a rectangular Grid.

{} <width> <height> <obstacles>
  <width> - The required grid width.
  <height> - The required grid height.
  <obstacles> - The number of random placed obstacles.\
"""


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 3:
        w, h, o = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        g = Grid(w, h, o)
        print(g.to_tgf())
    else:
        print(USAGE.format(sys.argv[0]))
