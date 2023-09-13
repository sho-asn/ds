package game.actions;

import edu.monash.fit2099.engine.actors.Actor;
import game.actors.Player;

/**
 * Purchasable interface that is implemented in the item that player want to purchase
 * @author Shosuke Asano
 */
public interface Purchasable {

    /**
     * purchase action of the player
     *
     * @param player a player who do purchase action
     */
    String actorPurchaseAction(Player player);
}
