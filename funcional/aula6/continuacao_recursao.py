def stringpali(str):
	return palindromo([c for c in str if c not in ' ,-.;'])



def concatena(l1, l2):
	if not l1 or not l2:
		return l1+l2
	elif l1[0] < l2[0]:
		return [l1[0]] + concatena(l1[1:], l2)
	else:
		return[l2[0]] + concatena(l1, l2[1:])

def mergesort(lst):
	if len(lst) < 2:
		return lst
	else:
		l1 = lst[:len(lst)/2]
		l2 = lst[len(lst)/2:]
		sl1 = mergesort(l1)
		sl2 = mergesort(l2)
		return concatena(sl1, sl2)


def mergesort2(lst):
	if len(lst) < 2:
		return lst
	else:
		return concatena(mergesort2(lst[:len(lst)/2]),mergesort2(lst[len(lst)/2:]))

def mapr(f, lst):
	if lst==[]:
		return []
	else:
		return [f(lst[0])] + mapr(f, lst[1:])


def somall(lst):
	if not lst:
		return 0
	elif type(lst[0]) == list:
		return somall(lst[0]) + somall(lst[1:])
	else:
		return lst[0] + somall(lst[1:])

print mergesort2([2,5,3,10,9,8,1,7])
