pairs = [[2, 1], [-2, -1]]
new_pairs = map(lambda p: sorted(p), pairs)
print(list(new_pairs)[0][0])        # 1
print(pairs)

b_pairs = map(lambda p: sorted(p), pairs)
print(list(b_pairs))

print()
lb = [(-1, 4), (5, -3), (2, -2)]
n_lb = map(lambda p: sorted(p), lb)
print(list(n_lb)[0][0]) # -1

n_lb = map(lambda p: sorted(p), lb)
print(list(n_lb)) #

# plattform... (processor - plattform) two answer..
# instance variables in class.__dict__ ¡?..

class Volume:
    chapter = 1
    def __init__(self, paragraph):
        self.paragraph = paragraph
        Volume.chapter += 1

    def remove(self):
        del self.paragraph

edition = Volume(1)
edition.remove()

print()
print(Volume.__dict__)
print()
print(edition.__dict__)
