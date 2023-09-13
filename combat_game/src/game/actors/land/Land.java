package game.actors.land;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.Status;
import game.actors.Enemy;
/**
 * Enemy for Land type
 * @author Shosuke Asano
 *
 */
public abstract class Land extends Enemy {

    /**
     * Constructor for Land class
     *
     * @param name        the name of the enemy
     * @param displayChar the character that will represent the enemy in the display
     * @param hitPoints   the enemy's starting hit points
     */
    public Land(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.addCapability(Status.LAND);
    }


    /**
     * This type of enemy does not have intrinsic weapon.
     *
     * @return null
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return null;
    }
}
