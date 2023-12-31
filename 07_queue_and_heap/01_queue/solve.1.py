def solve(cmd, queue):
    if cmd[0] == "enqueue":
        queue.append(cmd[1])
    elif cmd[0] == "dequeue":
        print("Oops!" if len(queue) == 0 else queue.pop(0))
    elif cmd[0] == "peek":
        print("None!" if len(queue) == 0 else queue[0])
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(len(queue) == 0)


N = int(input())
queue = []
for _ in range(N):
    cmd = input().split()
    solve(cmd, queue)
