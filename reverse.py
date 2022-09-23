

list_ =[[1, 2], [3, 4], [5, 6, 7]]


def reverse(list_):
  list_=list_[::-1]

  reverselist = [list_[i][::-1] for i in range(len(list_)) ]
  return reverselist

print(reverse(list_))
