from langgraph.graph import StateGraph, START, END

from graph.state import State
from graph.agents.discovery_node import discovery_node


graph_builder = StateGraph(State)

graph_builder.add_node("discovery", discovery_node)

graph_builder.add_edge(START, "discovery")
graph_builder.add_edge("discovery", END)

discovery_graph = graph_builder.compile()