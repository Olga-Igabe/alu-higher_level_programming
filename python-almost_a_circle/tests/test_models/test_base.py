class TestBaseSaveAndLoad(unittest.TestCase):
    """Tests for Base.save_to_file and Base.load_from_file."""

    def tearDown(self):
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_save_and_load_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_one_rectangle(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_no_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())

    def test_square_save_none(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_empty_list(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_one(self):
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_square_load_no_file(self):
        self.assertEqual(Square.load_from_file(), [])
