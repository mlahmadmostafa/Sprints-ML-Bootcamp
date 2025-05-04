from collections import Counter, namedtuple, deque
text = "To be or not to be that is the question"
print(Counter(text.split()))

record = namedtuple('book', ['title', 'author', 'year', 'ISBN'])
book1 = record('The Alchemist', 'Paulo Coelho', 1988, '1234567890')
print(book1.title)

queue = deque(['a', 'b', 'c', 'd', 'e'])
print("Queue:", queue)
queue.append('f')
print("Queue after append:", queue)
queue.popleft()
print("Queue after popleft:", queue)
