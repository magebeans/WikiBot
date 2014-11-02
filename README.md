Wikibot
=======

This is a bot I wrote in python to play the Wikipedia game. The idea of the game is to start at the article for an object A, and end at the article for another object B, prefarably completely unrelated, solely by following links from A. So, for example, if A has a link to C, which has a link to D, which has a link to B, the path A->C->D->B is a valid solution.

The populate function builds a graph of all possible outgoing links which the find function then does a DFS on to find a link between the two pages. 

It's still incredibly slow (I blame the Wikipedia API). I have to try multithreading this during the graph building phase to make it faster. The DFS is already pretty fast, and I think it works well.

Usage: python wiki.py \[Name of origin article\] \[Name of target article\]