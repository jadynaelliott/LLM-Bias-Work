import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

def build_weighted_undirected_network(scene_characters):
    """
    Build a weighted undirected interaction network based on character dialogues.
    """
    G = nx.Graph()
    # Count interactions (edges) between consecutive characters
    edge_weights = Counter((scene_characters[i], scene_characters[i + 1])
                            for i in range(len(scene_characters) - 1))
    
    # Add edges with weights to the graph
    for (char1, char2), weight in edge_weights.items():
        if G.has_edge(char1, char2):
            G[char1][char2]['weight'] += weight
        else:
            G.add_edge(char1, char2, weight=weight)
    
    return G

def plot_weighted_network(G, title):
    """
    Plot the weighted interaction network for a given scene.
    """
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Position nodes using a force-directed layout
    weights = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_size=2000, font_size=12, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    
    plt.title(title)
    plt.show()

def extract_character_order(scene_text):
    """
    Extract the chronological list of characters who speak in the given scene text.
    """
    # Regular expression to match character names (capitalized word(s) followed by a colon)
    character_pattern = re.compile(r"^\s*([A-Z][a-zA-Z\s]+):", re.MULTILINE)
    
    # Find all matches for character names in chronological order
    character_order = character_pattern.findall(scene_text)
    
    return character_order

# Example Scene Text
simple_scene_text = """
Alice: "Hey Beth, have you heard about the new event in town?"
Beth: "Yes, Cathy told me about it yesterday!"
Cathy: "It’s going to be exciting. Diana, are you coming too?"
Diana: "Absolutely, I wouldn’t miss it!"
"""

# Example Complex Scene Text
realistic_scene_text = """
Eve: "Hey, Frank, do you think the new marketing campaign will hit its goals?"
Frank: "I'm optimistic, but Grace had some concerns about the timing."
Grace: "Right, I think we need to coordinate better with the product team."
Eve: "That's fair. But Diana said we might have to push the launch anyway."
Diana: "Only if the new platform isn’t ready. Have we heard back from IT?"
Frank: "Not yet, Diana. I’ll follow up today."
Grace: "Maybe we should all sit down with IT and hash this out?"
Diana: "I agree, Grace. A meeting might save us time in the long run."
Eve: "Okay, but we can’t wait too long. Deadlines are coming up fast."
Frank: "Good point, Eve. Maybe we should set up a meeting for tomorrow?"
Grace: "Tomorrow works for me. What about you, Diana?"
Diana: "I’m in. Eve, can you send out the invite?"
Eve: "Sure thing. Let’s include the IT team and loop in product as well."
Frank: "Perfect. Hopefully, this gets everyone on the same page."
"""


if __name__ == "__main__":
    # Extract the chronological list of characters for the realistic scene
    character_order = extract_character_order(simple_scene_text)

    # Output the result
    print("Chronological List of Characters (Simple Scene):", character_order)

    # Build the weighted undirected network
    simple_network = build_weighted_undirected_network(character_order)

    # Plot the network
    plot_weighted_network(simple_network, "Realistic Scene: Weighted Undirected Network")

    # Extract the chronological list of characters for the realistic scene
    realistic_character_order = extract_character_order(realistic_scene_text)

    # Output the result
    print("Chronological List of Characters (Realistic Scene):", realistic_character_order)

    # Build the weighted undirected network
    realistic_scene_network = build_weighted_undirected_network(realistic_character_order)

    # Plot the network
    plot_weighted_network(realistic_scene_network, "Realistic Scene: Weighted Undirected Network")
