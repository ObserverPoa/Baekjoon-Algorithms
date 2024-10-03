'''
게임판 그래프를 구성하고, 
4개의 말 중 매번 한개를 선택해서 10회 움직이는 모든 경우를 탐색해서, 최대 점수를 구한다.
동일한 dfs 함수 호출을 방지하기 위해서 visited를 사용한다.
'''
import sys

input = sys.stdin.readline

class Node:
    def __init__(self, score = 0, next_red = None, next_blue = None):
        self.score = score
        self.next_red = next_red # 빨간색 화살표로 가리키는 노드
        self.next_blue = next_blue # 파란색 화살표로 가리키는 노드

# start에서 end까지 step씩 더하는 점수로 노드들을 생성하고 연결해서 반환
def create_nodes(start, end, step):
    nodes = [Node(start)]
    for score in range(start + step, end, step):
        node = nodes[-1].next_red = Node(score)
        nodes.append(node)
    return nodes

# 게임판 노드들을 생성하고 연결하는 함수
def create_board():
    start_node = Node()
    end_node = Node()
    center_node = Node(25)

    main_path_nodes = create_nodes(2, 41, 2)
    start_node.next_red = main_path_nodes[0]
    main_path_nodes[-1].next_red = end_node

    for node in main_path_nodes:
        nodes = []
        if node.score == 10:
            nodes = create_nodes(13, 20, 3)
        elif node.score == 20:
            nodes = create_nodes(22, 25, 2)
        elif node.score == 30:
            nodes = create_nodes(28, 25, -1)
        
        if nodes:
            node.next_blue = nodes[0]
            nodes[-1].next_red = center_node

    center_out_nodes = create_nodes(30, 36, 5)
    center_node.next_red = center_out_nodes[0]
    center_out_nodes[-1].next_red = main_path_nodes[-1]

    return (start_node, end_node)


dices = list(map(int, input().split()))

start_node, end_node = create_board()

max_total_score = 0

visited = set()

def dfs(turn, total_score, piece_nodes: list[Node]): 
    global max_total_score

    # 동일한 파라미터로 함수 호출을 한 적이 있다면 즉시 리턴한다.
    key = tuple([turn, total_score, *sorted(map(id, piece_nodes))])
    if key in visited:
        return
    visited.add(key)

    # 주사위를 다 굴렸다면 최대 점수 갱신
    if turn >= len(dices):
        max_total_score = max(max_total_score, total_score)
        return
    
    dice = dices[turn]

    for i, node in enumerate(piece_nodes):
        # 파란색 화살표 이동 처리
        if node.next_blue is not None:
            node = node.next_blue
        elif node.next_red is not None:
            node = node.next_red

        # 주사위-1 만큼 이동
        for _ in range(dice - 1):
            if node.next_red is None:
                break
            node = node.next_red

        # 마지막 노드이거나, 다른 말이 없는 노드인 경우
        if node == end_node or node not in piece_nodes:
            next_piece_nodes = piece_nodes[:]
            next_piece_nodes[i] = node
            dfs(turn + 1, total_score + node.score, next_piece_nodes)

dfs(0, 0, [start_node] * 4)

print(max_total_score)