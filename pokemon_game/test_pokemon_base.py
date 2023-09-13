import unittest
from tester_base import TesterBase


class TestPokemonBase(TesterBase):

    def test_get_HP(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            HP = c.get_HP()
            if HP != 7:
                self.verificationErrors.append(f"get_HP method did not return correct HP: {HP}")
        except Exception as e:
            self.verificationErrors.append(f"get_HP method failed. {e}")

    def test_set_HP(self):

        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            b.set_HP(20)
            if b.HP != 20:
                self.verificationErrors.append(f"set_HP method did not assign value correctly: {b.HP}")
        except Exception as e:
            self.verificationErrors.append(f"set_HP method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                b.set_HP("TEST")
        except Exception as e:
            self.verificationErrors.append(f"set_HP method failed. {e}")

    def test_reduce_HP(self):

        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s.reduce_HP(5)
            if s.HP != 3:
                self.verificationErrors.append(
                    f"reduce_HP method did not reduce HP correctly, Pokemon's HP after reducing HP: {s.HP}")
        except Exception as e:
            self.verificationErrors.append(f"reduce_HP failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                s.reduce_HP("TEST")
        except Exception as e:
            self.verificationErrors.append(f"reduce_HP failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                s.reduce_HP(-5)
        except Exception as e:
            self.verificationErrors.append(f"reduce_HP failed. {e}")

    def test_get_level(self):

        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            lvl = c.get_level()
            if lvl != 1:
                self.verificationErrors.append(f"get_level method did not return correct level: {lvl}")
        except Exception as e:
            self.verificationErrors.append(f"get_level method failed. {e}")

    def test_set_level(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            b.set_level(20)
            if b.level != 20:
                self.verificationErrors.append(f"set_level method did not assign level correctly: {b.level}")
        except Exception as e:
            self.verificationErrors.append(f"set_level method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                b.set_level("TEST")
        except Exception as e:
            self.verificationErrors.append(f"set_level method failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                b.set_level(-5)
        except Exception as e:
            self.verificationErrors.append(f"set_level method failed. {e}")

    def test_set_poke_type(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s.set_poke_type("Fire")
            if s.poke_type != "Fire":
                self.verificationErrors.append(
                    f"set_poke_type method did not assign pokemon's type correctly: {s.poke_type}")
        except Exception as e:
            self.verificationErrors.append(f"set_poke_type method failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                s.set_poke_type("Electric")
        except Exception as e:
            self.verificationErrors.append(f"set_poke_type method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                s.set_poke_type(5)
        except Exception as e:
            self.verificationErrors.append(f"set_poke_type method failed. {e}")

    def test_get_poke_type(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            type = c.get_poke_type()
            if type != "Fire":
                self.verificationErrors.append(f"get_poke_type method did not return correct type: {type}")
        except Exception as e:
            self.verificationErrors.append(f"get_poke_type method failed. {e}")

    def test_get_name(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            name = b.get_name()
            if name != "Bulbasaur":
                self.verificationErrors.append(f"get_name method did not return name correctly: {name}")
        except Exception as e:
            self.verificationErrors.append(f"get_name method failed. {e}")

    def test_get_speed(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            spd = s.get_speed()
            if spd != 7:
                self.verificationErrors.append(f"get_speed method did not return speed correctly: {spd}")
        except Exception as e:
            self.verificationErrors.append(f"get_speed method failed. {e}")

    def test_set_speed(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            c.set_speed(10)
            if c.speed != 10:
                self.verificationErrors.append(f"set_speed method did not assign speed correctly: {c.speed}")
        except Exception as e:
            self.verificationErrors.append(f"set_speed method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                c.set_speed("TEST")
        except Exception as e:
            self.verificationErrors.append(f"set_speed method failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                c.set_speed(-5)
        except Exception as e:
            self.verificationErrors.append(f"set_speed method failed. {e}")

    def test_get_defence(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            defence = b.get_defence()
            if defence != 5:
                self.verificationErrors.append(f"get_defence method did not return defence correctly: {defence}")
        except Exception as e:
            self.verificationErrors.append(f"get_defence method failed. {e}")

    def test_set_defence(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s.set_defence(20)
            if s.defence != 20:
                self.verificationErrors.append(f"set_defence method did not assign defence correctly: {s.defence}")
        except Exception as e:
            self.verificationErrors.append(f"set_defence method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                s.set_defence("TEST")
        except Exception as e:
            self.verificationErrors.append(f"set_defence method failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                s.set_defence(-10)
        except Exception as e:
            self.verificationErrors.append(f"set_defence method failed. {e}")

    def test_get_attack(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            atk = c.get_attack()
            if atk != 7:
                self.verificationErrors.append(f"get_attack method did not return attack correctly: {atk}")
        except Exception as e:
            self.verificationErrors.append(f"get_attack method failed. {e}")

    def test_set_attack(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            b.set_attack(20)
            if b.attack != 20:
                self.verificationErrors.append(f"set_attack method did not assign attack correctly: {b.attack}")
        except Exception as e:
            self.verificationErrors.append(f"set_attack method failed. {e}")
            return
        try:
            with self.assertRaises(TypeError):
                b.set_attack("TEST")
        except Exception as e:
            self.verificationErrors.append(f"set_attack method failed. {e}")
            return
        try:
            with self.assertRaises(ValueError):
                b.set_attack(-20)
        except Exception as e:
            self.verificationErrors.append(f"set_attack method failed. {e}")

    def test_alive(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            if s.alive() != True:
                self.verificationErrors.append(f"alive method did not return boolean correctly: {s.alive()}")
        except Exception as e:
            self.verificationErrors.append(f"alive method failed. {e}")

    def test_faint(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            c.HP = 0
            if c.faint() != True:
                self.verificationErrors.append(f"faint method did not return boolean correctly: {c.faint()}")
        except Exception as e:
            self.verificationErrors.append(f"faint method failed. {e}")

    def test_string(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            s = str(b)
            if s != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"string method did not return string correctly: {s}")
        except Exception as e:
            self.verificationErrors.append(f"string method failed. {e}")

    def test_faster_than(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            if c.faster_than(s) != True:
                self.verificationErrors.append(
                    f"faster_than method did not return boolean correctly: {c.faster_than(s)}")
        except Exception as e:
            self.verificationErrors.append(f"faster_than method failed. {e}")
        try:
            a = 5
            with self.assertRaises(TypeError):
                s.faster_than(a)
        except Exception as e:
            self.verificationErrors.append(f"faster_than method failed. {e}")

    def test_level_up(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            c.level_up()
            if c.level != 2 or c.attack != 8 or c.speed != 9 or c.HP != 7 or c.defence != 4:
                self.verificationErrors.append(
                    f"level_up method did not assign stats correctly: {c.level, c.attack, c.speed, c.defence, c.HP}")
        except Exception as e:
            self.verificationErrors.append(f"level_up method failed. {e}")

    def test_attacked_by(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            b.attacked_by(c)
            if b.faint() != True:
                self.verificationErrors.append(
                    f"attacked_by method did not execute correctly, state of Bulbasaur after attacked by Charmander: {b.faint()}")
        except Exception as e:
            self.verificationErrors.append(f"attacked_by method failed. {e}")
            return
        try:
            a = 5
            with self.assertRaises(TypeError):
                b.attacked_by(a)
        except Exception as e:
            self.verificationErrors.append(f"attacked_by method failed. {e}")

    def test_damage_taken(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            dmg = s.damage_taken(b)
            if dmg != 5:
                self.verificationErrors.append(f"damage_taken method did not return damage taken correctly: {dmg}")
        except Exception as e:
            self.verificationErrors.append(f"damage_taken method failed. {e}")
            return
        try:
            a = 5
            with self.assertRaises(TypeError):
                b.damage_taken(a)
        except Exception as e:
            self.verificationErrors.append(f"damage_taken method failed. {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
