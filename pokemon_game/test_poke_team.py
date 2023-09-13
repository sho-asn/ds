import unittest
from tester_base import TesterBase, captured_output

class TestPokeTeam(TesterBase):

    def test_PokeTeam(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Brock")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        if p.trainer != "Brock" or p.battle_mode != 0:
            self.verificationErrors.append(f"PokeTeam constructor did not assign attributes properly: {p.trainer, p.battle_mode}")

    def test_set_trainer(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            p.set_trainer("Misty")
            if p.trainer != "Misty":
                self.verificationErrors.append(f"set_trainer method did not assign trainer correctly: {p.trainer}")
        except Exception as e:
            self.verificationErrors.append(f"set_trainer method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                p.set_trainer(2)
        except Exception as e:
            self.verificationErrors.append(f"set_trainer method failed. {e}")

    def test_set_battle_mode(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            p.set_battle_mode(2)
            if p.battle_mode != 2:
                self.verificationErrors.append(f"set_battle_mode method did not assign battle mode correctly: {p.battle_mode}")
        except Exception as e:
            self.verificationErrors.append(f"set_battle_mode method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                p.set_battle_mode("TEST")
        except Exception as e:
            self.verificationErrors.append(f"set_battle_mode method failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                p.set_battle_mode(3)
        except Exception as e:
            self.verificationErrors.append(f"set_battle_mode method failed. {e}")

    def test_set_criterion(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            p.set_criterion("hp")
            if p.criterion != "hp":
                self.verificationErrors.append(f"set_criterion method did not assign criterion correctly: {p.criterion}")
        except Exception as e:
            self.verificationErrors.append(f"set_criterion method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                p.set_criterion(5)
        except Exception as e:
            self.verificationErrors.append(f"set_criterion method failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                p.set_criterion("unknown")
        except Exception as e:
            self.verificationErrors.append(f"set_criterion method failed. {e}")

    def test_get_trainer(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Cynthia")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            name = p.get_trainer()
            if name != "Cynthia":
                self.verificationErrors.append(f"get_trainer method did not return trainer name correctly: {name}")
        except Exception as e:
            self.verificationErrors.append(f"get_trainer method failed. {e}")

    def test_get_criterion(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            p.criterion = "hp"
            criterion = p.get_criterion()
            if criterion != "hp":
                self.verificationErrors.append(f"get_criterion method did not return criterion correctly: {criterion}")
        except Exception as e:
            self.verificationErrors.append(f"get_criterion method failed. {e}")

    def test_get_battle_mode(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            bm = p.get_battle_mode()
            if bm != 0:
                self.verificationErrors.append(f"get_battle_mode method did not return criterion correctly: {bm}")
        except Exception as e:
            self.verificationErrors.append(f"get_battle_mode method failed. {e}")

    def test_choose_team(self):
        from poke_team import PokeTeam
        try:
            p = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
        from poke_team import PokeTeam
        try:
            team = PokeTeam("Lance")
        except Exception as e:
            self.verificationErrors.append(f"Lance's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("11111\n2 2 2") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Lance's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokeTeam)
    unittest.TextTestRunner(verbosity=0).run(suite)