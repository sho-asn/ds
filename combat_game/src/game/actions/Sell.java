package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actors.Player;

/**
 * An Action to sell.
 * @author Shosuke Asano
 *
 */
public class Sell extends Action {

    /**
     * Sell interface
     */
    Sellable sellable;

    /**
     * The constructor for Sell
     *
     */
    public Sell(Sellable sellable) {
        this.sellable = sellable;
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
     * The weapon item that the actor decided to sell is removed form the weapon inventory.
     *
     * @param actor The actor performing the sell action.
     * @param map The map the actor is on.
     * @return The string message to show which item was sold.
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        String result = "";
        if (isPlayer(actor)) {
            Player player = (Player) actor;
            result = sellable.actorSellAction(player);
        }
        return result;
    }

    /**
     * Describes which weapon item can be sold by the actor.
     *
     * @param actor The actor performing the sell action.
     * @return a description used for the menu UI
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " can sell " + sellable;
    }
}
