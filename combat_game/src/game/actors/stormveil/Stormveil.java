package game.actors.stormveil;

import game.Status;
import game.actors.Enemy;

/**
 * Enemy for Stormveil type
 * @author Shosuke Asano
 *
 */
public abstract class Stormveil extends Enemy {
    /**
     * Constructor for Stormveil class
     *
     * @param name        the name of the Actor
     * @param displayChar the character that will represent the Actor in the display
     * @param hitPoints   the Actor's starting hit points
     */
    public Stormveil(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.addCapability(Status.STORMVEIL);
    }
}

