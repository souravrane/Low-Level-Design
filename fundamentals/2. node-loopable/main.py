from node import Node

if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20, node1)
    node3 = Node(30, node2)
    node4 = Node(40, node3)

    # iterate using for each loop
    for data in node4:
        print(data)