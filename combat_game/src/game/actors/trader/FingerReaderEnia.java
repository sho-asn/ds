package game.actors.trader;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.*;
import game.weapons.AxeOfGodrick;
import game.weapons.GraftedDragon;

/**
 * Trader Finger Reader Enia to allow player to sell and exchange
 * @author Shosuke Asano
 *
 */
public class FingerReaderEnia extends Actor{

    /**
     * Axe Of Godrick weapon that player can exchage
     */
    private AxeOfGodrick axeOfGodrick;
    /**
     * Grafted Dragon weapon that player can exchange
     */
    private GraftedDragon graftedDragon;

    /**
     * Constructor for FingerReaderEnia
     *
     */
    public FingerReaderEnia() {
        super("Finger Reader Enia ", 'E', 1);
        this.axeOfGodrick = new AxeOfGodrick();
        this.graftedDragon = new GraftedDragon();
    }

    /**
     * At each turn, Finger Reader Enia does not anything.
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
     * Returns a new sell and exchange actions that a player can.
     *
     * @param otherActor the Actor that might be performing attack
     * @param direction  String representing the direction of the other Actor
     * @param map        current GameMap
     * @return A collection of Actions.
     */
    public ActionList allowableActions(Actor otherActor, String direction, GameMap map) {
        ActionList actions = super.allowableActions(otherActor, direction, map);
        if (otherActor.hasCapability(Status.HOSTILE_TO_ENEMY)) {
            for (WeaponItem weaponItem : otherActor.getWeaponInventory()) {
                if (weaponItem.hasCapability(Status.SELLABLE)) {
                    actions.add(new Sell((Sellable) weaponItem));
                }
            }
            for (Item item : otherActor.getItemInventory()) {
                if (item.hasCapability(Status.EXCHANGEABLE)) {
                    actions.add(new Exchange((Exchangeable) item, axeOfGodrick));
                    actions.add(new Exchange((Exchangeable) item, graftedDragon));
                }
            }
        }
        return actions;
    }
}

