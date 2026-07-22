class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation."""

    def test_width_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_width_zero(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_width_negative(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as cm:
            r.width = -10
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_x_not_int(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as cm:
            r.x = {}
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_ctor_width_string(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_ctor_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_ctor_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_ctor_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_ctor_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_ctor_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
