package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actors.Player;

/**
 * Exchange items with another item
 * @author Shosuke Asano
 *
 */
public class Exchange extends Action {
    /**
     * Exchangeable interface
     */
    Exchangeable exchangeable;
    /**
     * purchasable interface
     */
    Purchasable purchasable;

    /**
     * The constructor for exchange
     *
     * @param exchangeable the item that actor want to exchange
     * @param purchasable the item that actor want to get
     */
    public Exchange(Exchangeable exchangeable, Purchasable purchasable) {
        this.exchangeable = exchangeable;
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
     * Implement exchange action
     * @param actor The actor performing the exchange action.
     * @param map The map the actor is on.
     * @return String representing the item that player got
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        String result = "";
        if (isPlayer(actor)) {
            Player player = (Player) actor;
            exchangeable.actorExchangeAction(player);
            result = purchasable.actorPurchaseAction(player);
        }
        return result;
    }

    /**
     * Describe which item can exchange
     *
     * @param actor The actor performing the exchange action.
     * @return the menu description
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " can exchange " + purchasable;
    }
}

