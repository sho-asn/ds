package game.actors.ocean;

import game.Status;
import game.actors.Enemy;
/**
 * Enemy for Ocean type
 * @author Shosuke Asano
 *
 */
public abstract class Ocean extends Enemy {
    /**
     * Constructor for Ocean class
     *
     * @param name        the name of the enemy
     * @param displayChar the character that will represent the enemy in the display
     * @param hitPoints   the enemy's starting hit points
     */
    public Ocean(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.addCapability(Status.OCEAN);
        this.addCapability(Status.HOSTILE_TO_ALL_ENEMY);
    }
}
