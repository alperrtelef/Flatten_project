

def flatten(n):
    for i in n:
        if isinstance(i,list):
            flatten(i)
        else:
            empty_list.append(i)
      
n=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
empty_list = []
flatten(n)
print(empty_list)
