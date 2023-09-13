package game.classes;

import game.weapons.Uchigatana;


/**
 * Class representing a Samurai role
 *
 * @author Ashi Dhandia
 */
public class Samurai extends CombatArchetypes {

    /**
     * Constructor for Samurai
     * Assigns the weapon and HP for this role
     */
    public Samurai() {
        super(new Uchigatana(), 455);
    }
}
