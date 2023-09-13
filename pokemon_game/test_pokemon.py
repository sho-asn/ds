import unittest
from tester_base import TesterBase


class TestPokemon(TesterBase):

    def test_Charmander(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        if c.level != 1 or c.HP != 7 or c.attack != 7 or c.defence != 4 or c.speed != 8 or c.poke_type != "Fire":
            self.verificationErrors.append(f"Charmander constructor did not assign stats properly: {c.name, c.level, c.HP, c.attack, c.defence, c.speed}")


    def test_Bulbasaur(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        if b.level != 1 or b.HP != 9 or b.attack != 5 or b.defence != 5 or b.speed != 7 or b.poke_type != "Grass":
            self.verificationErrors.append(f"Bulbasaur constructor did not assign stats properly: {b.name, b.level, b.HP, b.attack, b.defence, b.speed}")

    def test_Squirtle(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        if s.level != 1 or s.HP != 8 or s.attack != 4 or s.defence != 7 or s.speed != 7 or s.poke_type != "Water":
            self.verificationErrors.append(
                f"Squirtle constructor did not assign stats properly: {s.name, s.level, s.HP, s.attack, s.defence, s.speed}")

    def test_missing_no(self):
        from pokemon import MissingNo
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        if m.level != 1 or m.HP != 8 or m.attack != 5 or m.defence != 5 or m.speed != 7 or m.poke_type != None:
            self.verificationErrors.append(f"MissingNo constructor did not assign stats properly: {m.name, m.level, m.HP, m.attack, m.defence, m.speed}")

    def test_superpower(self):
        from pokemon import MissingNo
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            m.superpower()
            if (m.level != 2 or m.HP != 10) and (m.HP != 9 or m.level != 1) and (m.level != 2 or m.HP != 9):
                self.verificationErrors.append(f"Superpower did not assign stats properly: {m.name, m.level, m.HP, m.attack, m.defence, m.speed}")
        except Exception as e:
            self.verificationErrors.append(f"Superpower method failed: {str(e)}.")



    def test_increase_HP(self):
        from pokemon import MissingNo
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            m.increase_HP()
            if m.HP != 9:
                self.verificationErrors.append(f"MissingNo's HP should be 9: {m.HP}")
        except Exception as e:
            self.verificationErrors.append(f"increase HP method failed: {str(e)}.")
            return
        try:
            with self.assertRaises(TypeError):
                m.increase_HP("no")
        except Exception as e:
            self.verificationErrors.append(f"increase HP method failed: {str(e)}.")
            return
        try:
            with self.assertRaises(ValueError):
                m.increase_HP(-5)
        except Exception as e:
            self.verificationErrors.append(f"increase HP method failed: {str(e)}.")








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)