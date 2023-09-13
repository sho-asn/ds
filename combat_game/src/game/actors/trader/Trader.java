package game.actors.trader;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.actors.ActorLocationsIterator;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.AttackAction;
import game.actions.Purchase;
import game.actions.Sell;
import game.actions.Sellable;
import game.weapons.*;

import java.util.ArrayList;
import java.util.List;
/**
 * Trader class to allow player to purchase and sell
 * @author Shosuke Asano
 *
 */
public class Trader extends Actor {
    /**
     * great Knife that trader can sell
     */
    private GreatKnife greatKnife;
    /**
     * club that trader can sell
     */
    private Club club;
    /**
     * uchigatana that trader can sell
     */
    private Uchigatana uchigatana;

    /**
     * HeavyCrossbow that trader can sell
     */
    private HeavyCrossbow heavyCrossbow;

    /**
     * Scimitar that trader can sell
     */
    private Scimitar scimitar;
    /**
     * Constructor for Trader.
     *
     */
    public Trader() {
        super("Merchant Kale",'K',1);
        this.greatKnife = new GreatKnife();
        this.club = new Club();
        this.uchigatana = new Uchigatana();
        this.heavyCrossbow = new HeavyCrossbow();
        this.scimitar = new Scimitar();
    }


    /**
     * At each turn, trader does not anything.
     *
     * @param actions    collection of possible Actions for this Actor
     * @param lastAction The Action this Actor took last turn. Can do interesting things in conjunction with Action.getNextAction()
     * @param map        the map containing the Actor
     * @param display    the I/O object to which messages may be written
     * @return DoNothingAction()
     */
    @Override
    public Action playTurn(ActionList actions, Action lastAction, GameMap map, Display display) {
        return new DoNothingAction();
    }

    /**
     * Returns a new sell and purchase actions that a player can.
     *
     * @param otherActor the Actor that might be performing attack
     * @param direction  String representing the direction of the other Actor
     * @param map        current GameMap
     * @return A collection of Actions.
     */
    public ActionList allowableActions(Actor otherActor, String direction, GameMap map) {
        ActionList actions = super.allowableActions(otherActor, direction, map);
        if (otherActor.hasCapability(Status.HOSTILE_TO_ENEMY)) {
            actions.add(new Purchase(uchigatana));
            actions.add(new Purchase(greatKnife));
            actions.add(new Purchase(club));
            actions.add(new Purchase(heavyCrossbow));
            actions.add(new Purchase(scimitar));
            for (WeaponItem weaponItem : otherActor.getWeaponInventory()) {
                if (weaponItem.hasCapability(Status.SELLABLE)) {
                    actions.add(new Sell((Sellable) weaponItem));
                }
            }
        }
        return actions;
    }
}
