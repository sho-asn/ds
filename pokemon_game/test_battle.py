import unittest
from tester_base import TesterBase, captured_output

class TestBattle(TesterBase):

    def test_set_mode_battle(self):
        from battle import Battle

        try:
            b = Battle("Red", "Blue")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("6 0 0\n0 6 0") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Red"
        except AssertionError:
            self.verificationErrors.append(f"Red should win: {result}.")
            return
        try:
            assert str(b.team1) == "Charmander's HP = 7 and level = 7, Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    def test_rotating_mode_battle(self):
        from battle import Battle

        try:
            b = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n1 2 2") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Brock"
        except AssertionError:
            self.verificationErrors.append(f"Brock should win: {result}.")
        try:
            assert str(b.team1) == "Squirtle's HP = 5 and level = 1, Charmander's HP = 7 and level = 3, Bulbasaur's HP = 5 and level = 2, Bulbasaur's HP = 6 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    def test_battle_example(self):
        from battle import Battle

        try:
            b = Battle("Cynthia", "Steven")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n1 2 2") as (inp, out, err):
                result = b.optimised_mode_battle("atk", "def")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Steven"
        except AssertionError:
            self.verificationErrors.append(f"Steven should win: {result}.")
        try:
            assert str(b.team2) == "Bulbasaur's HP = 2 and level = 3, Charmander's HP = 7 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team1)}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBattle)
    unittest.TextTestRunner(verbosity=0).run(suite)