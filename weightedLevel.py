def weightSum(rootNode):
    sum = 0

    level = 1
    queue = [rootNode]
    length = len(queue)

    while(len(queue)):
        length = len(queue)
        for i in range(length):
            currNode = queue.deque()
        sum += currNode.value * level
        for children in currNode.childrens:
        queue.enque(children)

        level += 1

    return sum
