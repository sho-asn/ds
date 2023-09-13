package game.classes;

import game.weapons.AstrologerStaff;


/**
 * Class representing an Astrologer role
 *
 * @author Ashi Dhandia
 */
public class Astrologer extends CombatArchetypes {

    /**
     * Constructor for Astrologer
     * Assigns the weapon and HP for this role
     */
    public Astrologer() {
        super(new AstrologerStaff(), 396);
    }
}
