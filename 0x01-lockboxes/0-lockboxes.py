def canUnlockAll(boxes):
    if not boxes:
        return False

    visited = [False] * len(boxes)
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

# # Test cases
# boxes1 = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes1))  # Output: True

# boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes2))  # Output: True

# boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes3))  # Output: False
