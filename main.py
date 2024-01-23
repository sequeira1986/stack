'''STACKmôžete použiť list na simuláciu zásobníka použitím metód append() na
pridanie prvku na koniec zoznamu a pop() na odstránenie posledného prvku
zoznamu.'''
stack = []
stack.append("fero")
stack.append("Joso")
stack.append("lucia")
print(stack)
stack.pop(-1)
print(stack)

'''QUEUE použiť list na simuláciu fronty pomocou metódy append() na pridanie prvku na
koniec zoznamu a metódy pop() na odstránenie prvého prvku zo zoznamu'''
queue =[]
queue.append("allan")
queue.append("jose")
queue.append("pedro")
print(queue)
queue.pop(-3)
print(queue)
