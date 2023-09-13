package game.actors.wind;

import game.Status;
import game.actors.Enemy;
/**
 * Enemy for Wind type
 * @author Shosuke Asano
 *
 */
public abstract class Wind extends Enemy {
    /**
     * Constructor for Wind class
     *
     * @param name        the name of the enemy
     * @param displayChar the character that will represent the enemy in the display
     * @param hitPoints   the enemy's starting hit points
     */
    public Wind(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.addCapability(Status.WIND);
    }
}
