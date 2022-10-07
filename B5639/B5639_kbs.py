arr =[]
tree = {}

while True:
    try:
        a = int(input())
        arr.append(a)

    except:
        break

root = arr[0]
tree[root] = [None, None, None]

def push_l(p_node, x):
    if tree[p_node][1]==None:
        tree[x] = [p_node, None, None]
        tree[p_node][1] = x
    elif x<tree[p_node][1]:
        push_l(tree[p_node][1],x)
    else:
        push_r(tree[p_node][1],x)


def push_r(p_node, x):
    if tree[p_node][2]==None:
        tree[x] = [p_node, None, None]
        tree[p_node][2] = x
    elif x>tree[p_node][2]:
        push_r(tree[p_node][2],x)
    else:
        push_l(tree[p_node][2],x)


def post_order(node):
    _,l,r= tree[node]

    if l:post_order(l)
    if r:post_order(r)

    print(node)


for x in arr[1:]:
    if x < root: push_l(root, x)
    else: push_r(root, x)

post_order(root)