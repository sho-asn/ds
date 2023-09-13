package game.weapons;

import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

/**
 * A weapon that can be used to attack the enemy.
 * It deals 115 damage with 85% hit rate
 * @author Shosuke Asano
 *
 */
public class Grossmesser extends WeaponItem implements Sellable {
    /**
     * the sell price of Grossmesser
     */
    private final int SELL_PRICE = 100;

    /**
     * Constructor
     */
    public Grossmesser(){
        super("Grossmesser", '?', 115, "hit", 85);
        this.addCapability(Status.HOSTILE_TO_ALL_ENEMY);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * get the sell price of Grossmesser
     * @return the sell price of Grossmesser
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }

    /**
     * Player will get runes of the sell price
     *
     * @param player a player who do sell action
     * @return String representing that the description of sell
     */
    @Override
    public String actorSellAction(Player player) {
        String result;
        player.removeWeaponFromInventory(this);
        player.pickUpRunes(this.getSELL_PRICE());
        result = "Player sold Grossmesser";
        return result;
    }
}
