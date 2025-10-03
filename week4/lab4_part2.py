from typing import Optional
from collections import deque

class DLLN:
    def __init__(self, contents):
        self.contents = contents
        self.prev: Optional[DLLN] = None
        self.next: Optional[DLLN] = None

    def __repr__(self):
        return f"This node contains: {self.contents}"

    def insertAfter(self, contents):
        newNode = DLLN(contents)

        if self.next is None:
            newNode.prev = self
            self.next = newNode
        else:
            newNode.prev = self
            newNode.next = self.next
            self.next.prev = newNode
            self.next = newNode

        return newNode

    def insertBefore(self, contents):
        newNode = DLLN(contents)

        if self.prev is None:
            newNode.next = self
            self.prev = newNode
        else:
            newNode.next = self
            newNode.prev = self.prev
            self.prev.next = newNode

        return newNode

    def toList(self):
        allContents = deque([self.contents])
        left = self.prev
        right = self.next

        while left is not None:
            allContents.appendleft(left.contents)
            left = left.prev
        while right is not None:
            allContents.append(right.contents)
            right = right.next
        
        return list(allContents)

    def findLast(self):
        curr = self

        while curr.next is not None:
            curr = curr.next
        
        return curr

    def findFirst(self):
        curr = self

        while curr.prev is not None:
            curr = curr.prev
        
        return curr

    def findAfter(self, needle):
        maybeNeedle = self.next

        while maybeNeedle is not None and maybeNeedle.contents != needle:
            maybeNeedle = maybeNeedle.next
        
        if maybeNeedle is None:
            raise KeyError("that needle can't be found after this node")
        return maybeNeedle

    def findBefore(self, needle):
        maybeNeedle = self.prev

        while maybeNeedle is not None and maybeNeedle.contents != needle:
            maybeNeedle = maybeNeedle.prev
        
        if maybeNeedle is None:
            raise KeyError("that needle can't be found before this node")
        return maybeNeedle


def main():
    one = DLLN("one")
    two = one.insertAfter('two')
    print("should be one two:", one.toList())

    five = one.findLast().insertAfter('five')
    print("should be one two five:", one.toList())

    three = two.insertAfter('three')
    print("should be one two three five:", one.toList())

    zero = one.insertBefore('zero')
    print("should be zero one two three five:", one.findFirst().toList())

    four = one.findAfter('five').insertBefore('four')
    print("should be zero one two three four five:", one.findFirst().toList())

    the_two = one.findFirst().findAfter('two')
    print("should successfully find two:", the_two)

    the_two = one.findLast().findBefore('two')
    print("should successfully find two:", the_two)


    print("should fail to find two:")
    try:
        print(two.findBefore('two'), "this should not print")
    except KeyError as ke:
        print("KEY ERROR", ke)


if __name__ == "__main__":
    main()
