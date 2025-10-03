from lab4_part1 import LLN
from typing import List


def reverse(lln: LLN):
    nodes: List[LLN] = []

    curr = lln
    while curr is not None:
        nodes.append(curr)
        curr = curr.next

    if len(nodes) <= 1:
        return nodes

    nodes[0].next = None
    for i in range(1, len(nodes)):
        nodes[i].next = nodes[i-1]
    
    return nodes[-1]

def main():
    first = LLN("one")
    second = first.insertAfter("two")
    third = first.findLast().insertAfter("three")
    fourth = first.findLast().insertAfter("four")

    print("before we reverse the list, starting at first:", first.toList())
    newBegin = reverse(first)
    print("now that we have reversed, the list from first is very short: ", first.toList())
    print("but the list from the new beginning is longer:", newBegin.toList())
    print("and since newBegin is fourth, here it is again:", fourth.toList())

    ### Here's the output:
    """
    before we reverse the list, starting at first: ['one', 'two', 'three', 'four']
    now that we have reversed, the list from first is very short:  ['one']
    but the list from the new beginning is longer: ['four', 'three', 'two', 'one']
    and since newBegin is fourth, here it is again: ['four', 'three', 'two', 'one']
    """


if __name__ == "__main__":
    main()
