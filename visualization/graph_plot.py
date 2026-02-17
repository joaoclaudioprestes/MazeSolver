import matplotlib.pyplot as plt
import networkx as nx


def plot_graph_path(
    graph, path=None, visit_order=None, start=None, end=None, title=None
):
    # Fixed position for nodes based on their coordinates (row, col)
    pos = {node: (node[1], -node[0]) for node in graph.nodes()}

    plt.figure(figsize=(6, 6))

    # Draw the graph
    nx.draw(
        graph,
        pos,
        node_size=200,
        node_color="lightblue",
        with_labels=False,
        edge_color="gray",
    )

    # Visit nodes
    if visit_order:
        nx.draw_networkx_nodes(
            graph, pos, nodelist=visit_order, node_color="yellow", node_size=150
        )

    # The final path
    if path:
        edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color="red", width=2)
        nx.draw_networkx_nodes(
            graph, pos, nodelist=path, node_color="orange", node_size=200
        )

    # Start e End
    if start:
        nx.draw_networkx_nodes(
            graph, pos, nodelist=[start], node_color="green", node_size=250
        )
    if end:
        nx.draw_networkx_nodes(
            graph, pos, nodelist=[end], node_color="red", node_size=250
        )

    if title:
        plt.title(title)
    plt.axis("off")
    plt.show()
