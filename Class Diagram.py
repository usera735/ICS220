import pygraphviz as pgv

# Create a new graph
G = pgv.AGraph(strict=True, directed=True)

# Add nodes
G.add_node("Passenger")
G.add_node("BoardingPass")
G.add_node("Flight")
G.add_node("CheckInSystem")

# Add attributes to nodes
G.get_node("Passenger").attr['shape'] = 'record'
G.get_node("Passenger").attr['label'] = "{ Passenger | -name : str\n-seat_number : str\n-flight_number : str }"

G.get_node("BoardingPass").attr['shape'] = 'record'
G.get_node("BoardingPass").attr['label'] = "{ BoardingPass | -passenger : Passenger\n-gate : str\n-departure_time : str }"

G.get_node("Flight").attr['shape'] = 'record'
G.get_node("Flight").attr['label'] = "{ Flight | -number : str\n-destination : str\n-terminal : str }"

G.get_node("CheckInSystem").attr['shape'] = 'record'
G.get_node("CheckInSystem").attr['label'] = "{ CheckInSystem | -flights : list }"

# Add edges
G.add_edge("Passenger", "BoardingPass", label="1..1")
G.add_edge("Passenger", "CheckInSystem", label="1..1")
G.add_edge("Flight", "BoardingPass", label="1..1")
G.add_edge("CheckInSystem", "Flight", label="1..*")

# Save the graph to a file
G.draw("class_diagram.png", prog="dot", format="png")