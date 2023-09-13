package game.classes;

import game.weapons.GreatKnife;


/**
 * Class representing a Bandit role
 *
 * @author Ashi Dhandia
 */
public class Bandit extends CombatArchetypes {

    /**
     * Constructor for Bandit
     * Assigns the weapon and HP for this role
     */
    public Bandit() {
        super(new GreatKnife(), 414);
    }
}
