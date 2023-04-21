import streamlit as st
import streamlit_canvas as st_canvas
import json

# Define the nodes of the flowchart
nodes = {
    "Start": {"x": 50, "y": 150},
    "Process 1": {"x": 200, "y": 50},
    "Process 2": {"x": 200, "y": 250},
    "End": {"x": 350, "y": 150},
}

# Define the connections between nodes
edges = [("Start", "Process 1"), ("Start", "Process 2"), ("Process 1", "End"), ("Process 2", "End")]

# Define the colors of the nodes and connections
node_color = {"Start": "green", "End": "red"}
edge_color = {"Start->Process 1": "blue", "Start->Process 2": "blue", "Process 1->End": "purple", "Process 2->End": "purple"}

def draw_flowchart():
    # Draw the nodes
    for node in nodes:
        color = node_color.get(node, "white")
        st_canvas.draw_rectangle(
            nodes[node]["x"],
            nodes[node]["y"],
            nodes[node]["x"] + 100,
            nodes[node]["y"] + 50,
            color=color,
            fill_color=color,
            stroke_width=2,
        )
        st_canvas.write_text(node, nodes[node]["x"] + 10, nodes[node]["y"] + 10)
    
    # Draw the connections between nodes
    for edge in edges:
        start_node = edge[0]
        end_node = edge[1]
        color = edge_color.get(f"{start_node}->{end_node}", "black")
        st_canvas.draw_line(
            nodes[start_node]["x"] + 100,
            nodes[start_node]["y"] + 25,
            nodes[end_node]["x"],
            nodes[end_node]["y"] + 25,
            color=color,
            width=2,
        )

def main():
    st.title("Interactive Flowchart")
    
    # Draw the initial flowchart
    draw_flowchart()
    
    # Allow users to modify the flowchart
    with st_canvas.StCanvas(draw_func=draw_flowchart, height=400, width=500, stroke_width=2, stroke_color="black", background_color="white", key="canvas"):
        if st_canvas._get_state().dirty:
            json_data = st_canvas._get_state().to_json()
            nodes_data = json.loads(json_data)["objects"]["nodes"]
            edges_data = json.loads(json_data)["objects"]["lines"]
            for node in nodes_data:
                nodes[node["text"]]["x"] = node["x"]
                nodes[node["text"]]["y"] = node["y"]
            for edge in edges_data:
                start_node = edge["start_text"]
                end_node = edge["end_text"]
                edges.append((start_node, end_node))
                edge_color[f"{start_node}->{end_node}"] = "black"

if __name__ == "__main__":
    main()
