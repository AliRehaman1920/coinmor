from langgraph.graph import StateGraph, START, END

from graph.state import State
from graph.agents.intelligence_node import intelligence_node


graph_builder = StateGraph(State)

graph_builder.add_node("intelligence", intelligence_node)

graph_builder.add_edge(START, "intelligence")
graph_builder.add_edge("intelligence", END)

intelligence_graph = graph_builder.compile()