def count_orbit_transitions(start, end, planets):
    x1, y1 = start
    x2, y2 = end
    transitions = 0

    for cx, cy, r in planets:
        # 출발점이 행성계 내부에 있는지 확인
        start_inside = (x1 - cx)**2 + (y1 - cy)**2 < r**2
        # 도착점이 행성계 내부에 있는지 확인
        end_inside = (x2 - cx)**2 + (y2 - cy)**2 < r**2
        
        # 출발점과 도착점의 상태가 다르면 진입/이탈이 발생
        if start_inside != end_inside:
            transitions += 1

    return transitions

# 입력 처리
T = int(input())  # 테스트 케이스 개수
results = []

for _ in range(T):
    # 출발점, 도착점
    x1, y1, x2, y2 = map(int, input().split())
    start = (x1, y1)
    end = (x2, y2)

    # 행성계 정보
    n = int(input())  # 행성계 개수
    planets = [tuple(map(int, input().split())) for _ in range(n)]

    # 진입/이탈 계산
    results.append(count_orbit_transitions(start, end, planets))

# 결과 출력
for result in results:
    print(result)