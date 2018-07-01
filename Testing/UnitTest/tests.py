import unittest
from activities import eat, nap


class ActivityTest(unittest.TestCase):
    # Do stuff here that needs to happen before each test
    def setUp(self):
        pass

    def test_eat_healthy(self):
        """Yay extra information about the test!"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "Broccoli is healthy."
        )

    def test_eat_unhealthy(self):
        """Explanations are awesome."""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "Pizza is not healthy."
        )

    def test_is_healthy_boolean(self):
        # This should reflect errors that are raised in the function
        # Expecting a value error when a string is passed in
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="a string")

    def test_short_nap(self):
        """You're failing! Go home."""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap."
        )

    def test_long_nap(self):
        """Hey look. It's the last one. Can we get beers now?"""
        self.assertEqual(
            nap(3),
            "Crap, I didn't mean to sleep 3 hours."
        )


if __name__ == "__main__":
    unittest.main()
