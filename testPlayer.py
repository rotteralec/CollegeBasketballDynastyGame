import unittest
import Player

class Test_TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        testPlayer = Player(13,"PG")
        return super().setUpClass()
        
    def test_PlayerInitialization(self):
        self.assertTrue(testPlayer.)




if __name__ == '__main__':
    unittest.main()