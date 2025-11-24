# ...existing code...
class _Node:
    __slots__ = ("value", "next")
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt
        
class LinkedList:
    """Singly linked list with common helpers."""
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self._length = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def append(self, value):
        """Add value to the end."""
        node = _Node(value)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self._length += 1

    def prepend(self, value):
        """Add value to the front."""
        node = _Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._length += 1

    def insert(self, index, value):
        """Insert value at index (0..len)."""
        if index < 0 or index > self._length:
            raise IndexError("index out of range")
        if index == 0:
            return self.prepend(value)
        if index == self._length:
            return self.append(value)
        prev = None
        cur = self.head
        for _ in range(index):
            prev, cur = cur, cur.next
        node = _Node(value, cur)
        prev.next = node
        self._length += 1

    def get(self, index):
        """Return value at index."""
        if index < 0 or index >= self._length:
            raise IndexError("index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.value

    def remove(self, value):
        """Remove first occurrence of value. Returns True if removed."""
        prev = None
        cur = self.head
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                if cur is self.tail:
                    self.tail = prev
                self._length -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def remove_at(self, index):
        """Remove and return value at index."""
        if index < 0 or index >= self._length:
            raise IndexError("index out of range")
        prev = None
        cur = self.head
        for _ in range(index):
            prev, cur = cur, cur.next
        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next
        if cur is self.tail:
            self.tail = prev
        self._length -= 1
        return cur.value

    def pop(self):
        """Remove and return last element (like remove_at(len-1))."""
        if self.is_empty():
            raise IndexError("pop from empty list")
        return self.remove_at(self._length - 1)

    def find(self, predicate_or_value):
        """
        Find first index matching predicate or equal to value.
        If argument is callable, it's used as predicate(value) -> bool.
        Returns index or -1 if not found.
        """
        pred = predicate_or_value
        is_callable = callable(pred)
        idx = 0
        cur = self.head
        while cur:
            if (is_callable and pred(cur.value)) or (not is_callable and cur.value == pred):
                return idx
            cur = cur.next
            idx += 1
        return -1

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    def clear(self):
        self.head = self.tail = None
        self._length = 0

    def reverse(self):
        """Reverse list in-place."""
        prev = None
        cur = self.head
        self.tail = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __repr__(self):
        return f"LinkedList({self.to_list()})"

# Examples demonstrating each method
if __name__ == "__main__":
    ll = LinkedList()
    print("empty:", ll, "len:", len(ll))

    # append
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("after append:", ll, "len:", len(ll))

    # prepend
    ll.prepend(5)
    print("after prepend:", ll)

    # insert
    ll.insert(2, 15)  # insert 15 at index 2
    print("after insert at 2:", ll)

    # get
    print("get(0):", ll.get(0))
    print("get(2):", ll.get(2))

    # find by value
    print("find(20):", ll.find(20))
    print("find(999):", ll.find(999))

    # find by predicate
    print("find(lambda x: x>15):", ll.find(lambda x: x > 15))

    # to_list and iteration
    print("to_list:", ll.to_list())
    print("iterating:", [x for x in ll])

    # remove by value
    removed = ll.remove(15)
    print("removed 15?", removed, ll)

    # remove_at
    val = ll.remove_at(1)
    print("removed at 1 ->", val, ll)

    # pop
    last = ll.pop()
    print("popped:", last, ll)

    # reverse
    ll.reverse()
    print("reversed:", ll)

    # clear
    ll.clear()
    print("cleared:", ll, "is_empty:", ll.is_empty())

# ...existing code...