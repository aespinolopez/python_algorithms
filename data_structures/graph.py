from collections import deque


class PersonGraph:
    def __init__(self):
        """
        Adjacency list implementation of a graph
        """
        graph = {}
        graph["me"] = ["alice", "bob", "claire"]
        graph["bob"] = ["anuj", "peggy"]
        graph["alice"] = ["peggy"]
        graph["claire"] = ["thom", "jonny"]
        graph["anuj"] = []
        graph["peggy"] = []
        graph["thom"] = []
        graph["jonny"] = []
        self.graph = graph

    def breadth_first_search(self, name, predicate):
        search_queue = deque()
        search_queue += self.graph[name]
        searched = []
        while search_queue:
            person = search_queue.popleft()
            if person not in searched:
                if predicate(person):
                    print("Founded!")
                    return True

                searched.append(person)
                search_queue += self.graph[person]

        return False
