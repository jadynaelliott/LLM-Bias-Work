# LLM-Bias-Work
This Python script extracts a chronological list of characters, so that we can build a weighted undirected graph to visualize which characters interact and how often. The primary goal of this tool is to provide an intuitive way to study character dynamics in scenes using Python libraries like networkx and matplotlib.

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


References: 
Agarwal, Apoorv, Jiehan Zheng, Shruti Kamath, Sriramkumar Balasubramanian, and Shirin Ann Dey (2015). “Key female characters in film have more to talk about besides men: Automating the bechdel test”. In: Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 830–840 (cit. on pp. 16–18, 20–22).
