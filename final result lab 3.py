import os


class BinaryTree:
    def __init__(self, value, left=None, right=None):  # ✅ виправлено
        self.value = value
        self.left = left
        self.right = right

    def print_tree(self):
        canvas = {}

        def draw(node, r, c, dir_x, h_step, v_step):
            if not node:
                return

            val_str = str(node.value)
            for i, char in enumerate(val_str):
                canvas[(r, c + i)] = char

            next_h = max(5, int(h_step * 0.75))
            next_v = max(4, int(v_step * 0.75))

            if node.left:
                symbol = "/" if dir_x == -1 else "\\"
                for i in range(1, v_step):
                    curr_r = r - i
                    curr_c = c + dir_x * int(i * (h_step / v_step))
                    canvas[(curr_r, curr_c)] = symbol

                draw(node.left, r - v_step, c + dir_x * h_step, dir_x, next_h, next_v)

            if node.right:
                symbol = "\\" if dir_x == -1 else "/"
                for i in range(1, v_step):
                    curr_r = r + i
                    curr_c = c + dir_x * int(i * (h_step / v_step))
                    canvas[(curr_r, curr_c)] = symbol

                draw(node.right, r + v_step, c + dir_x * h_step, dir_x, next_h, next_v)

        root_r, root_c = 0, 0
        val_str = str(self.value)
        for i, ch in enumerate(val_str):
            canvas[(root_r, root_c + i)] = ch

        if self.left:
            for i in range(1, 12):
                canvas[(root_r, root_c - i)] = "─"
            draw(self.left, root_r, root_c - 13, -1, 16, 12)

        if self.right:
            for i in range(1, 12):
                canvas[(root_r, root_c + len(val_str) + i - 1)] = "─"
            draw(self.right, root_r, root_c + 11 + len(val_str), 1, 16, 12)

        if not canvas:
            return

        min_r = min(r for r, c in canvas.keys())
        max_r = max(r for r, c in canvas.keys())
        min_c = min(c for r, c in canvas.keys())
        max_c = max(c for r, c in canvas.keys())

        print("\n")
        for r in range(min_r, max_r + 1):
            line = []
            for c in range(min_c, max_c + 1):
                line.append(canvas.get((r, c), " "))
            print("".join(line).rstrip())
        print("\n")


def build_from_simple_list(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    node = BinaryTree(arr[mid])
    node.left = build_from_simple_list(arr[:mid])
    node.right = build_from_simple_list(arr[mid + 1:])
    return node


def main():
    filename = "tree.txt"

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(" ".join(map(str, range(1, 21))))

    with open(filename, "r") as f:
        content = f.read().split()

    numbers = []
    for x in content:
        try:
            numbers.append(int(x))
        except ValueError:
            pass

    numbers.sort()

    root = build_from_simple_list(numbers)

    if root:
        root.print_tree()


if __name__ == "__main__":  # ✅ виправлено
    main()