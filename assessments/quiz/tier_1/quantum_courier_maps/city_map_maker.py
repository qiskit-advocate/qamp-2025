import os
import textwrap

MAP_TEXT = """
Quantum Courier — Sample City Map (Text Description)

Nodes:
  S = Start
  A, B, C = intersections
  G = Goal

Roads (with noise numbers):
  S - A  (2)
  S - B  (3)
  A - B  (1)
  A - C  (2)
  B - C  (2)
  B - G  (3)
  C - G  (1)

Example routes from S to G:
  Route 1: S -> A -> C -> G   (2 + 2 + 1 = 5)
  Route 2: S -> B -> G       (3 + 3 = 6)
  Route 3: S -> B -> C -> G  (3 + 2 + 1 = 6)
  Route 4: S -> A -> B -> G  (2 + 1 + 3 = 6)

Teachers can sketch this as dots and lines on paper or use it
to design a nicer printed map. Keep totals small and visible
so students can add them easily.
""".strip() + "\n"

def main(outdir="city_map"):
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "map_1.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MAP_TEXT)
    print("Wrote sample map description to:", os.path.abspath(path))

if __name__ == "__main__":
    main()
