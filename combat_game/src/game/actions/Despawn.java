package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;

/**
 * An Action to let enemies despawned
 *
 * @author Shosuke Asano
 *
 */
public class Despawn extends Action {
    /**
     * Constructor for Despawn class
     */
    public Despawn(){}

    /**
     * The enemy is removed from the map.
     *
     * @param actor The actor will be despawned.
     * @param map The map the actor is on.
     * @return The string message of the despawned enemy.
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        map.removeActor(actor);
        return actor + " is despawned from the map.";

    }

    /**
     * Nothing will be returned.
     *
     * @param actor The actor performing the action.
     * @return null
     */
    @Override
    public String menuDescription(Actor actor) {
        return null;
    }

}
