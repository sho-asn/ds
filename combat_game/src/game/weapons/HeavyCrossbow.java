package game.weapons;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

public class HeavyCrossbow extends WeaponItem implements Purchasable, Sellable {

    /**
     * the purchase price of Heavy Crossbow
     */
    private final int PURCHASE_PRICE = 1500;

    /**
     * the sell price of Heavy Crossbow
     */
    private final int SELL_PRICE = 100;

    /**
     * Constructor.
     */
    public HeavyCrossbow() {
        super("Heavy Crossbow", '}', 64, "shoots", 57);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * get the purchase price of Heavy Crossbow
     * @return the purchase price of Heavy Crossbow
     */
    public int getPURCHASE_PRICE() {
        return PURCHASE_PRICE;
    }

    /**
     * get the sell price of Heavy Crossbow
     * @return the sell price of Heavy Crossbow
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }

    /**
     * if player has enough runes, sdd heavy crossbow to inventory
     *
     * @param player a player who do purchase action
     * @return what item the player purchased
     */
    @Override
    public String actorPurchaseAction(Player player) {
        String result;
        if (player.getCurrentRunes() >= this.getPURCHASE_PRICE()) {
            player.useRunes(this.getPURCHASE_PRICE());
            result = "Player purchased Heavy Crossbow.";
            player.addWeaponToInventory(new HeavyCrossbow());
        }
        else {
            result = "Player does not have enough runes to purchase Heavy Crossbow.";
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
        result = "Player sold Heavy Crossbow";
        return result;
    }
}
