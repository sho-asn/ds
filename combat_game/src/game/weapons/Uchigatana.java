package game.weapons;

import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

/**
 * A weapon that can be used to attack the enemy.
 * It deals 115 damage with 80% hit rate
 * @author Shosuke Asano
 *
 */
public class Uchigatana extends WeaponItem implements Purchasable, Sellable {

    /**
     * the purchase price for Uchigatana
     */
    private final int PURCHASE_PRICE = 5000;
    /**
     * teh sell price for Uchigatana
     */
    private final int SELL_PRICE = 500;

    /**
     * Constructor
     */
    public Uchigatana() {
        super("Uchigatana", ')',115,"strikes",80);
        this.addCapability(Status.UCHIGATANA);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * get the purchase price of Uchigatana
     * @return the purchase price of Uchigatana
     */
    public int getPURCHASE_PRICE() {
        return PURCHASE_PRICE;
    }

    /**
     * get the sell price of Uchigatana
     * @return the sell price of Uchigatana
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }

    /**
     * if player has enough runes, add uchigatana to inventory
     *
     * @param player a player who do purchase action
     * @return what item the player purchased
     */
    @Override
    public String actorPurchaseAction(Player player) {
        String result;
        if (player.getCurrentRunes() >= this.getPURCHASE_PRICE()) {
            player.useRunes(this.getPURCHASE_PRICE());
            result = "Player purchased uchigatana.";
            player.addWeaponToInventory(new Uchigatana());
        }
        else {
            result = "Player does not have enough runes to purchase uchigatana.";
        }
        return result;
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
        result = "Player sold uchigatana";
        return result;
    }
}


