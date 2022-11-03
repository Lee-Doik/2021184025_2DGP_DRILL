# 0 : 뒤에 그려질 객체
# 1 : 앞에 그려질 객체
world = [[], []]


def add_object(o, depth):
    world[depth].append(o)


def remove_object(o):
    # world.remove(o)     # 리스트 에서만 삭제
    # del o               # 실제 메모리 공간 확보
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in world:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()
