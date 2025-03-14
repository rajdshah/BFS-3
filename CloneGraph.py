"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time Complexity : O(V + E)
# Space Complexity : O(V)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        nodemap = {}
        nodemap[node.val] = Node(val = node.val)
        paths = [node]
        while len(paths) > 0:
            curr = paths.pop()
            currcopy = nodemap[curr.val]
            for nbr in curr.neighbors:
                if nbr.val not in nodemap:
                    paths.append(nbr)
                    nodemap[nbr.val] = Node(val = nbr.val)
                currcopy.neighbors.append(nodemap[nbr.val])
        return nodemap[node.val]