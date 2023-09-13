package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import game.Status;
import game.actors.Player;

/**
 * An Action to purchase.
 * @author Shosuke Asano
 *
 */
public class Purchase extends Action {

    /**
     * Purchasable interface
     */
    Purchasable purchasable;


    /**
     * Constructor for Purchase
     *
     */
    public Purchase(Purchasable purchasable){
        this.purchasable = purchasable;
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
     * If the player has enough runes to buy the weapon item, he can purchase it.
     * Otherwise, the purchase fails.
     *
     * @param actor The actor performing purchase action.
     * @param map The map the actor is on.
     * @return The string message whether the purchase success or not.
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        String result = "";
        if (isPlayer(actor)) {
            Player player = (Player) actor;
            result = purchasable.actorPurchaseAction(player);
        }
        return result;
    }




    /**
     * Describes which weapon item may be purchased by the actor.
     *
     * @param actor The actor performing the purchase action.
     * @return a description used for the menu UI
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " can purchase " + purchasable;
    }
}
