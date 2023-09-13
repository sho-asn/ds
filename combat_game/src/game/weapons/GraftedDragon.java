package game.weapons;

import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Exchangeable;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

public class GraftedDragon extends WeaponItem implements Sellable, Purchasable {

    /**
     * the sell price of GraftedDragon
     */
    private final int SELL_PRICE = 200;

    /**
     * Constructor.
     *
     */
    public GraftedDragon() {
        super("Grafted Dragon", 'N', 89, "hits", 90);
        this.addCapability(Status.HOSTILE_TO_ALL_ENEMY);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * get the sell price of GraftedDragon
     * @return the sell price of GraftedDragon
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
        result = "Player sold Grafted Dragon";
        return result;
    }


    /**
     * add Grafted Dragon to inventory
     *
     * @param player a player who do purchase action
     * @return what item the player purchased
     */
    @Override
    public String actorPurchaseAction(Player player) {
        String result;
        result = "Player exchanged Grafted Dragon.";
        player.addWeaponToInventory(new GraftedDragon());
        return result;
    }
}
