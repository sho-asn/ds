package game.actors.fire;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.Status;
import game.actors.Enemy;
/**
 * Enemy for Fire type
 * @author Ashi Dhandia, Seah Thern Fong
 *
 */
public abstract class Fire extends Enemy {

    /**
     * Constructor for Fire class
     *
     * @param name        the name of the enemy
     * @param displayChar the character that will represent the enemy in the display
     * @param hitPoints   the enemy's starting hit points
     * @author Seah Thern Fong, Ashi Dhandia
     */
    public Fire(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.addCapability(Status.FIRE);
    }

}
