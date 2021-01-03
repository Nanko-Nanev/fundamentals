n = int(input())
shell = []
counter = 0

while n > 0:
    counter += 1
    capacity_for_shell_level = 2 * (counter ** 2)
    if capacity_for_shell_level <= n:
        shell.append(capacity_for_shell_level)
        n -= capacity_for_shell_level
    else:
        shell.append(n)
        break

print(shell)