import re
import networkx as nx
import matplotlib.pyplot as plt


def parse_graph(tikz_syntax: str):
    """
    Parse a minimal TikZ/graph block into a networkx DiGraph.
    Only supports 'A -> {B, D, E};' style.
    """
    G = nx.DiGraph()
    # split statements by ;
    statements = [s.strip() for s in tikz_syntax.split(';') if s.strip()]
    for stmt in statements:
        if '->' in stmt:
            left, right = stmt.split('->', 1)
            left = left.strip()
            right = right.strip().strip('{} ')
            nodes = [r.strip() for r in right.split(',')]
            for node in nodes:
                if node:
                    G.add_edge(left, node)
    return G


tikz_like = r"""
A -> {B, D, E};
B -> C;
D -> {C, E, F};
C -> F;
E -> F;
"""

# Parse to networkx
G = parse_graph(tikz_like)

# spring layout (like TikZ spring layout)
pos = nx.spring_layout(G, seed=42)  # deterministic with seed

# Draw
plt.figure(figsize=(5, 5))
nx.draw(G, pos, with_labels=True, node_size=800,
        node_color="lightblue", arrowsize=20,
        font_size=12, font_weight="bold")
plt.show()
