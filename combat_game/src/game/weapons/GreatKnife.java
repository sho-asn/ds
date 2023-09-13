package game.weapons;

import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

/**
 * A weapon that can be used to attack the enemy.
 * It deals 75 damage with 70% hit rate
 * @author Shosuke Asano
 *
 */
public class GreatKnife extends WeaponItem implements Purchasable, Sellable {

    /**
     * the purchase price of Great Knife
     */
    private final int PURCHASE_PRICE = 3500;
    /**
     * the sell price of Great Knife
     */
    private final int SELL_PRICE = 350;

    /**
     * Constructor
     */
    public GreatKnife() {
        super("Great Knife", '/', 75, "stabs", 70);
        this.addCapability(Status.GREAT_KNIFE);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * get the purchase price of Great Knife
     * @return the purchase price of Great Knife
     */
    public int getPURCHASE_PRICE() {
        return PURCHASE_PRICE;
    }

    /**
     * get the sell price of Great Knife
     * @return the sell price of Great Knife
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }

    /**
     * if player has enough runes, sdd great knife to inventory
     *
     * @param player a player who do purchase action
     * @return what item the player purchased
     */
    @Override
    public String actorPurchaseAction(Player player) {
        String result;
        if (player.getCurrentRunes() >= this.getPURCHASE_PRICE()) {
            player.useRunes(this.getPURCHASE_PRICE());
            result = "Player purchased great knife.";
            player.addWeaponToInventory(new GreatKnife());
        }
        else {
            result = "Player does not have enough runes to purchase great knife.";
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
        result = "Player sold Great Knife";
        return result;
    }
}


