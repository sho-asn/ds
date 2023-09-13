package game.actions;

import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.actors.Player;

/**
 * Exchange interface that is implemented in item class that player want to get
 * @author Shosuke Asano
 */
public interface Exchangeable {
    /**
     * exchange action of the player
     *
     * @param player a player who do exchange action
     */
    void actorExchangeAction(Player player);
}
