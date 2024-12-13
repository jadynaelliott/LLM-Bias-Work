import re
import networkx as nx
import matplotlib.pyplot as plt

def build_consecutive_network(scene_characters):
    """
    Build a directed interaction network based on consecutive character dialogues.
    """
    G = nx.DiGraph()
    # Add nodes (unique characters)
    G.add_nodes_from(scene_characters)
    
    # Add edges based on consecutive dialogues
    for i in range(len(scene_characters) - 1):
        G.add_edge(scene_characters[i], scene_characters[i + 1])
    
    return G

def plot_network(G, title):
    """
    Plot the character interaction network for a given scene.
    """
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_size=2000, font_size=12, font_weight="bold")
    plt.title(title)
    plt.show()


def extract_character_order(scene_text):
    """
    Extract the chronological list of characters who speak in the given scene text.
    """
    # Regular expression to match character names (capitalized word(s) followed by a colon)
    character_pattern = re.compile(r"^([A-Z][a-zA-Z\s]+):", re.MULTILINE)
    
    # Find all matches for character names in chronological order
    character_order = character_pattern.findall(scene_text)
    
    return character_order

# Example Scene Text
scene_text = """
Alice: "Hey Beth, have you heard about the new event in town?"
Beth: "Yes, Cathy told me about it yesterday!"
Cathy: "It’s going to be exciting. Diana, are you coming too?"
Diana: "Absolutely, I wouldn’t miss it!"
"""
if __name__ == "__main__":
    # Extract the chronological list of characters
    character_order = extract_character_order(scene_text)

    # Output the result
    print("Chronological List of Characters:", character_order)
    # Build the network
    network = build_consecutive_network(character_order)
        
    # Plot the network
    plot_network(network, f"Scene Example")
