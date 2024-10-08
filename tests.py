import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_tiny_cells(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 1, 1, None)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_open_close_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 1, 1, None)
        start = m1.cells[0][0]
        end = m1.cells[-1][-1]
        self.assertEqual(
            start.has_top,
            False,
        )
        self.assertEqual(
            end.has_bottom,
            False,
        )

    def test_maze_visited_reset(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 1, 1, None, None)
        start = m1.cells[0][0]
        end = m1.cells[-1][-1]
        self.assertEqual(
            start.visited,
            False,
        )
        self.assertEqual(
            end.visited,
            False,
        )


if __name__ == "__main__":
    unittest.main()
