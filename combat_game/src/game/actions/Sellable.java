package game.actions;

import edu.monash.fit2099.engine.actors.Actor;
import game.actors.Player;
/**
 * Sellable interface that is implemented in the item that player want to sell
 * @author Shosuke Asano
 */
public interface Sellable {
    /**
     * sell action of the player
     *
     * @param player a player who do sell action
     */
    String actorSellAction(Player player);
}
