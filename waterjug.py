from collections import deque

def water_jug_solver(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0, [])])

    while queue:
        current_a, current_b, steps = queue.popleft()

        if (current_a, current_b) == target:
            return steps

        if (current_a, current_b) not in visited:
            visited.add((current_a, current_b))

            # Fill jug A and B
            queue.append((capacity_a, current_b, steps + [(current_a, current_b, "Fill jug A")]))
            queue.append((current_a, capacity_b, steps + [(current_a, current_b, "Fill jug B")]))

            # Empty jug A and B
            queue.append((0, current_b, steps + [(current_a, current_b, "Empty jug A")]))
            queue.append((current_a, 0, steps + [(current_a, current_b, "Empty jug B")]))

            # Pour water from A to B
            pour_amount = min(current_a, capacity_b - current_b)
            queue.append((current_a - pour_amount, current_b + pour_amount, steps + [(current_a, current_b, "Pour water from jug A to jug B")]))

            # Pour water from B to A
            pour_amount = min(current_b, capacity_a - current_a)
            queue.append((current_a + pour_amount, current_b - pour_amount, steps + [(current_a, current_b, "Pour water from jug B to jug A")]))

    return None

def main():
    capacity_a = int(input("Enter the capacity of jug A: "))
    capacity_b = int(input("Enter the capacity of jug B: "))
    target = tuple(map(int, input("Enter the target amount of water: ").split()))

    solution = water_jug_solver(capacity_a, capacity_b, target)

    if solution:
        print("Solution Path:")
        for step in solution:
            print(f"Jug A: {step[0]}, Jug B: {step[1]}, Action: {step[2]}")
    else:
        print("No solution")

main()
