package game.weapons;

import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

/**
 * A weapon that can be used to attack the enemy.
 * It deals 118 damage with 88% hit rate
 * @author Shosuke Asano
 *
 */
public class Scimitar extends WeaponItem implements Sellable, Purchasable {
    /**
     * the purchase price of Scimitar
     */
    private final int PURCHASE_PRICE = 600;
    /**
     * the sell price of Scimitar
     */
    private final int SELL_PRICE = 100;

    /**
     * Constructor for Scimitar
     */
    public Scimitar() {
        super("Scimitar", 's', 118, "hit", 88);
        this.addCapability(Status.HOSTILE_TO_ALL_ENEMY);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * get the purchase price of Scimitar
     * @return the purchase price of Scimitar
     */
    public int getPURCHASE_PRICE() {
        return PURCHASE_PRICE;
    }

    /**
     * get the sell price of Scimitar
     * @return the sell price of Scimitar
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }

    /**
     * if player has enough runes, add scimitar to inventory
     *
     * @param player a player who do purchase action
     * @return what item the player purchased
     */
    @Override
    public String actorPurchaseAction(Player player) {
        String result;
        if (player.getCurrentRunes() >= this.getPURCHASE_PRICE()) {
            player.useRunes(this.getPURCHASE_PRICE());
            result = "Player purchased Scimitar.";
            player.addWeaponToInventory(new Scimitar());
        }
        else {
            result = "Player does not have enough runes to purchase Scimitar.";
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
        result = "Player sold Scimitar";
        return result;
    }
}
