import unittest
from tester_base import TesterBase,captured_output

class TestReferentialArray(TesterBase):

    def test_bubble_sort(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1") as (inp, out, err):
                p.choose_team(2, "hp")
        except Exception as e:
            self.verificationErrors.append(f"Choose team failed to execute: {str(e)}.")
            return
        try:
            assert str(p) == "Bulbasaur's HP = 9 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Bubble sort is wrong, PokeTeam after sorting: {str(p)}.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReferentialArray)
    unittest.TextTestRunner(verbosity=0).run(suite)