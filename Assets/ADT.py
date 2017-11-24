def makeQueue():
 	return ('Queue', [])

def isQueue(obj): 
	return type(obj) == type(()) and obj[0] == 'Queue'
		
def queueContents(q):
	return q[1]

def enqueue(q,el):
	if isQueue(q):
		queueContents(q).append(el)
	else:
		raise TypeError("enqueue : Not a Queue")

def dequeue(q):
	if not isQueueEmpty(q):
		return queueContents(q).pop(0)
	else:
		raise IndexError("Queue is Empty")

def isQueueEmpty(q):
	if isQueue(q):
		return queueContents(q) == []
	else:
		raise TypeError("arg must be a queue")

def front(q):
	if isQueue(q):
		return queueContents(q)[0]
	else:
		raise TypeError("dequeue: arg must be a queue")

def isStack(obj):
	return type(obj) == type(()) and obj[0] == 'Stack'

def makeStack():
	return ('Stack', [])

def stackContents(s):
	return s[1]

def push(s, el):
	if isStack(s):
		stackContents(s).insert(0, el)
	else:
		raise TypeError("push: First arg must be a stack")

def pop(s):
	if isStack(s):
		return stackContents(s).pop(0)
	else:
		raise TypeError("pop: arg must be a stack")

def top(s):
	if isStack(s):
		return stackContents(s)[0]
	else:
		raise TypeError("top: arg must be a stack")

def isStackEmpty(s):
	if isStack(s):
		return stackContents(s) == []
	else:
		raise TypeError("isStackEmpty: arg must be a stack")

def reverseStack(oldStack):
	n = len(oldStack[1])
	reversedStack = makeStack()
	for _ in range(n):
		push(reversedStack, pop(oldStack))
	return reversedStack
