import wikipedia
import sys
from collections import defaultdict

def main():
    args = sys.argv
    if(len(args) < 3):
        print "Need two arguments"

    fr = args[1]
    to = args[2]

    try:
        fr = wikipedia.page(fr)
        g = Graph(fr)
        print "-"*80
        print "Populating the tree"
        g.visited = defaultdict(lambda: False)
        g.populate(g.root,3)
        print "Done populating the tree"
        print "-"*80
        print "Finding path"
        g.visited = defaultdict(lambda: False)
        g.find(to, g.root,3)
        print "-"*80
    except wikipedia.exceptions.PageError:
        print "No such page, try again"

class Graph:
    root = ""
    nodes = defaultdict(list)
    visited = defaultdict(lambda: False)
     
    def __init__(self, root):
        self.root= root.title
        self.nodes[self.root] = root.links

    def populate(self, node=root, levels=6):
        self.visited[self.root] = True
        print " "*(6-levels), "Visiting ", node.encode('utf-8', errors='replace'), " with ", len(self.nodes[node]), " neighbours"
        if levels > 0:
            for neighbour in self.nodes[self.root]:
                if(self.visited[neighbour] == False):
                    # print "\t",neighbour
                    try:
                        self.nodes[neighbour] += wikipedia.page(neighbour).links
                    except wikipedia.exceptions.DisambiguationError as e:
                        self.nodes[neighbour] += wikipedia.page(e.options[0]).links
                    self.visited[neighbour] = True
                    self.populate(neighbour,levels-1)

    def find(self, to, fr=root, levels=6):
        pre = " "*(6-levels)
        self.visited[fr] = True
        # print pre,"Seaching from: " , fr.decode("utf-8")
        if levels <= 0:
            return fr == to 
        for neighbour in self.nodes[fr]:
            if(not self.visited[neighbour]):
                if(self.find(to, neighbour, levels-1)):
                    print pre,"Part of chain: ", fr, "=>" ,neighbour
                    return True
                self.visited[neighbour] = True

main()