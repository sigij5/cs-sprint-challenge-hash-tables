#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tix = dict((x.source, x.destination) for x in tickets)
    visited = {}
    route = []
    cur = tix['NONE']
    while cur not in visited:
        # print(cur)
        visited[cur] = 0
        route.append(cur)
        cur = tix[cur]
    # print(tix)
    print(route)
    return route
