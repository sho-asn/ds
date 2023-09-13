package game.classes;

import game.weapons.Club;


/**
 * Class representing a Wretch role
 *
 * @author Ashi Dhandia
 */
public class Wretch extends CombatArchetypes {

    /**
     * Constructor for Wretch
     * Assigns the weapon and HP for this role
     */
    public Wretch() {
        super(new Club(), 414);
    }
}
