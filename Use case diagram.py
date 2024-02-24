import pygraphviz as pgv

# Create a new graph
G = pgv.AGraph(strict=True, directed=True)

# Add nodes
G.add_node("Passenger")
G.add_node("Check-In Agent")
G.add_node("Boarding Gate Agent")
G.add_node("System")

# Add edges
G.add_edge("Passenger", "System", label="Check-in")
G.add_edge("Check-In Agent", "System", label="Check-in")
G.add_edge("System", "Boarding Gate Agent", label="Boarding")
G.add_edge("Passenger", "System", label="Boarding")

# Save the graph to a file
G.draw("use_case_diagram.png", prog="dot", format="png")
