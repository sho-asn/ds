package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import game.Status;
import game.actors.Player;

/**
 * It provides consume item action
 * @author Seah Thern Fong
 *
 * Modified by: Shosuke Asano
 */
public class ConsumeAction extends Action{

    /**
     * Consumable interface
     */
    private Consumable consumable;

    /**
     * The constructor for consume action
     *
     * @param consumable consumable interface
     */
    public ConsumeAction(Consumable consumable) {
        this.consumable = consumable;
    }

    /**
     * Check whether the actor is player or not
     *
     * @param actor actor that consume item
     * @return boolean if the actor is player or not
     */
    public boolean isPlayer(Actor actor) {
        return actor.hasCapability(Status.HOSTILE_TO_ENEMY);
    }

    /**
     * The item is consumed by the actor
     *
     * @param actor The actor performing consume action.
     * @param map The map the actor is on.
     * @return String representing
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        String result = "";
        if (isPlayer(actor)) {
            Player player = (Player) actor;
            consumable.consume(player);
            result = actor + " consumed " + consumable;
        }
        return result;
    }

    /**
     * Describe which item can consume
     *
     * @param actor The actor performing the consume action.
     * @return the menu description of consume action
     */
    @Override
    public String menuDescription (Actor actor){
        return actor + " can consume " + consumable;
    }
}


