# Cellular-Automaton-Explorer
A janky python program that lets you explore all 2^512 possible 2d binary cellular automata with 9 neighbours.

Each rule can be specified by a 512 bit binary string where each bit represents the result of applying the rule to a cell with that configuration of neighbours.
For example, a 1 in the 47th bit means that if the neighbours of a cell (including itself) look like the binary representation of 47
000
101
111
then it should change to 1.

## Controls

Press left and right to go to the next or previous rule. Press 1 to increase the special step and press 2 to decrease it. Press up and down to increase or decrease by the special step.

Press n for a randomly selected rule with a proportion of 1:4 1's to 0's.

Press r to reset the current rule with a random starting configuration.

Press s to save the current rule.

Press l to load a rule (opens the python terminal and gives you a list to select from)

Press e to enter a rule in either base 64 (using alphanumeric characters as well as "@" and "&")

Press c to toggle between slowly cycling through rules every 10 seconds (120 frames at 12fps)

---

© Copyright Caspar Monckton 2024
