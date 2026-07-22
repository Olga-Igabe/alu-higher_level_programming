class TestSquareInit(unittest.TestCase):
    """Tests for Square instantiation."""

    def test_is_rectangle_instance(self):
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_width_equals_height(self):
        s = Square(5)
        self.assertEqual(s.width, s.height)

    def test_all_args(self):
        s = Square(5, 1, 2, 99)
        expected = (5, 5, 1, 2, 99)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id), expected)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_ctor_size_string(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_ctor_x_string(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_ctor_y_string(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_ctor_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_ctor_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_ctor_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_ctor_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)
