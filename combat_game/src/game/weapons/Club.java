package game.weapons;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.Purchasable;
import game.actions.Sellable;
import game.actors.Player;

/**
 * A simple weapon that can be used to attack the enemy.
 * It deals 103 damage with 80% hit rate
 * Created by:
 * @author Adrian Kristanto
 * Modified by: Shosuke Asano
 *
 */
public class Club extends WeaponItem implements Purchasable, Sellable {
    /**
     * the purchase price of club
     */
    private final int PURCHASE_PRICE = 600;
    /**
     * the sell price of club
     */
    private final int SELL_PRICE = 100;

    /**
     * Constructor
     */
    public Club() {
        super("Club", '!', 103, "bonks", 80);
        this.addCapability(Status.SELLABLE);
    }

    /**
     * Count the turn
     * @param currentLocation The location of the actor carrying this Item.
     * @param actor The actor carrying this Item.
     */
    @Override
    public void tick(Location currentLocation, Actor actor) {}

    /**
     * get the purchase price of club
     * @return the purchase price of club
     */
    public int getPURCHASE_PRICE() {
        return PURCHASE_PRICE;
    }

    /**
     * get the sell price of club
     * @return the sell price of club
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }

    /**
     * if player has enough runes, sdd club to inventory
     *
     * @param player a player who do purchase action
     * @return what item the player purchased
     */
    @Override
    public String actorPurchaseAction(Player player) {
        String result;
        if (player.getCurrentRunes() >= this.getPURCHASE_PRICE()) {
            player.useRunes(this.getPURCHASE_PRICE());
            result = "Player purchased club.";
            player.addWeaponToInventory(new Club());
        }
        else {
            result = "Player does not have enough runes to purchase club.";
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
        result = "Player sold Club";
        return result;
    }
}
