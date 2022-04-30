def max_num(a,b,c):
  return max([a,b,c])


def mult_list(lst):

  if len(lst) == 0:
    return 0

  prod = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod

def rev_string(my_str):
  return my_str[::-1]

def num_within(x,a,b):
  return x in range(a,b+1)
     
t = [[1],[1,1]]
def pascal(n):
    if n < 1:
        return
    elif n == 1:
        print(t[0])
    else:
        r = 2
        while len(t) < n:
            row = []
            previous_row = t[r - 1]
            l = len(previous_row)+1
            for i in range(l):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < l-1:
                    row.append(t[r-1][i-1]+t[r-1][i])
                else:
                    row.append(1)
            print(row)
            t.append(row)
            r += 1

#testing 
t = [[1],[1,1]]
pascal(5)
