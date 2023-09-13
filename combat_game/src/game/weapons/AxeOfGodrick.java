package game.weapons;

import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Exchangeable;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

public class AxeOfGodrick extends WeaponItem implements Sellable, Purchasable {
    /**
     * the sell price of AxeOfGodrick
     */
    private final int SELL_PRICE = 100;

    /**
     * Constructor.
     *
     */
    public AxeOfGodrick() {
        super("Axe of Godrick", 'T', 142, "hits", 84);
        this.addCapability(Status.HOSTILE_TO_ALL_ENEMY);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * get the sell price of AxeOfGodrick
     * @return the sell price of AxeOfGodrick
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
        result = "Player sold Axe of Godrick";

        return result;
    }

    /**
     * Add AxeOfGodrick to inventory
     *
     * @param player a player who do purchase action
     * @return what item the player purchased
     */
    @Override
    public String actorPurchaseAction(Player player) {
        String result;
        result = "Player exchanged Axe of Godrick.";
        player.addWeaponToInventory(new AxeOfGodrick());
        return result;
    }
}
