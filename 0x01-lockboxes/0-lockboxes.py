#!/usr/bin/python3
"""Lockboxes Task"""


def canUnlockAll(boxes):
    """Initialize the set of opened boxes and the list of keys we have"""
    opened_boxes = set([0])
    keys = boxes[0]

    # Iterate while we have keys to process
    while keys:
        key = keys.pop()
        if key not in opened_boxes and key < len(boxes):
            opened_boxes.add(key)
            keys.extend(boxes[key])

    # Check if we've opened all boxes
    return len(opened_boxes) == len(boxes)
