# LLM-Bias-Work
Character Network Builder Code

This Python script extracts a chronological list of characters from a scene in a script, builds a directed interaction network using the consecutive method (Agarwal et al. 2015), and visualizes the network using matplotlib and networkx.

The script's features: 
* Identifies character names based on the script, formatted as:
  * Character Name: "Dialogue"
* Creates a directed graph where nodes represent characters and directed edges represent consecutive dialogue interactions.
* Displays the interaction network for the scene using MatPlotLib.

References: 
Agarwal, Apoorv, Jiehan Zheng, Shruti Kamath, Sriramkumar Balasubramanian, and Shirin Ann Dey (2015). “Key female characters in film have more to talk about besides men: Automating the bechdel test”. In: Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 830–840 (cit. on pp. 16–18, 20–22).
