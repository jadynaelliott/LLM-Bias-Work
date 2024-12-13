# LLM-Bias-Work
This Python script was developed as part of a project to analyze interactions between characters in a script. By extracting a chronological list of characters, we can build a weighted undirected graph to visualize which characters interact and how often. The primary goal of this tool is to provide an intuitive way to study character dynamics in scenes using Python libraries like networkx and matplotlib.

Thought Process Behind the Script
The idea for this script started with the challenge of understanding how characters interact within a given scene. Initially, the focus was on using a directed graph to represent who speaks to whom. However, after reflecting on the research goals, it became clear that the direction of interaction wasn’t as important as simply knowing whether two characters had interacted. This realization led to pivoting toward a weighted undirected graph, which better represents the relationships without overcomplicating the analysis.

Additionally, it became apparent that counting the frequency of interactions between characters (edge weights) would provide meaningful insights into the strength of relationships. For example, characters who speak to each other multiple times in a scene likely have a stronger connection, and this should be reflected in the graph.

Challenges and Adjustments
Parsing Dialogue:
At first, parsing the script seemed straightforward, but handling variations in formatting required designing a reliable regular expression.
Scripts often have leading spaces or inconsistent formatting, so the regex was adjusted to account for these variations.
Graph Design:
The decision to move from a directed to an undirected graph simplified the analysis while still capturing meaningful data.
Edge weights were added to highlight repeated interactions, making the graph more informative.
These adjustments made the script more practical for research, focusing on simplicity and flexibility.

Features
Character Extraction
Identifies character names based on lines formatted as:
plaintext
Copy code
Character Name: "Dialogue"
Outputs a chronological list of characters in the order they speak.
Weighted Undirected Graph
Creates a graph where:
Nodes represent characters.
Edges represent interactions between characters.
Weights indicate the frequency of interactions.
Visualization
Displays the network using matplotlib with:
Nodes labeled by character names.
Edge weights shown to represent interaction frequency.
Installation
To run this script, make sure you have Python installed, along with the necessary libraries:

References: 
Agarwal, Apoorv, Jiehan Zheng, Shruti Kamath, Sriramkumar Balasubramanian, and Shirin Ann Dey (2015). “Key female characters in film have more to talk about besides men: Automating the bechdel test”. In: Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 830–840 (cit. on pp. 16–18, 20–22).
