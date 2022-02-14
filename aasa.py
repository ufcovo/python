def parent(num):
    def first():
        return 1
    
    def second():
        return 2
    if num == 1:
        return first
    else:
        return second
x = parent(2)
print(x())