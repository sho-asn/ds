package game.items;

import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Exchangeable;
import game.actions.Sellable;
import game.actors.Player;
import game.weapons.AxeOfGodrick;
import game.weapons.GraftedDragon;
/**
 * Remembrance Of The Grafted allow a player to exchange item
 * @author Shosuke Asano
 */
public class RemembranceOfTheGrafted extends Item implements Sellable, Exchangeable {


    /**
     * the sell price of RemembranceOfTheGrafted
     */
    private final int SELL_PRICE = 20000;

    /***
     * Constructor for RemembranceOfTheGrafted
     *
     */
    public RemembranceOfTheGrafted() {
        super("Remembrance of the Grafted", 'O', true);
        this.addCapability(Status.SELLABLE);
        this.addCapability(Status.EXCHANGEABLE);
    }

    /**
     * get the sell price of RemembranceOfTheGrafted
     * @return the sell price of RemembranceOfTheGrafted
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }

    /**
     * Player will get runes of the sell price
     *
     * @param player what item the player sold
     * @return String representing that the description of sell
     */
    @Override
    public String actorSellAction(Player player) {
        String result;
        player.pickUpRunes(this.getSELL_PRICE());
        result = "Player sold Remembrance of the Grafted";
        return result;
    }


    /**
     * RemembranceOfTheGrafted will be removed from the inventory
     * @param player what item player exchanged
     */
    @Override
    public void actorExchangeAction(Player player) {
        player.removeItemFromInventory(this);
    }
}
