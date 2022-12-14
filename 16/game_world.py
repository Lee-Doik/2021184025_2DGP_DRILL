# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[], []]

# collision information
# key 'boy:balls' string
# value [ [boy] , [ball1, ball2, ball3] ]
collision_group = dict()


def add_object(o, depth):
    objects[depth].append(o)


def add_objects(ol, depth):
    objects[depth] += ol


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            # 충돌 오브젝트 그룹에서도 제거해야 함
            remove_collision_object(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in objects:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()


def add_collision_pairs(a, b, group):
    if group not in collision_group:
        print("add new group")
        collision_group[group] = [[], []]

    if a:
        if type(a) == list:
            collision_group[group][0] += a  # list 이므로 더함
        else:
            collision_group[group][0].append(a)  # 단일 object 면 추가
    if b:
        if type(b) == list:
            collision_group[group][1] += b  # list 이므로 더함
        else:
            collision_group[group][1].append(b)  # 단일 object 면 추가


def all_collision_pairs():
    for group, pairs in collision_group.items():  # key, value 값 모두를 가져옴
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group


def remove_collision_object(o):
    for pairs in collision_group.values():  # 키는 필요 없음
        if o in pairs[0]:
            pairs[0].remove(o)
        elif o in pairs[1]:
            pairs[1].remove(o)
