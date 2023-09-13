package game.actors;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actions.AreaAttackAction;
import game.actions.AttackAction;
import game.actions.QuickstepAction;
import game.actions.UnsheatheAction;
import game.behaviours.AttackBehaviour;
import game.behaviours.Behaviour;
import game.behaviours.WanderBehaviour;
import game.classes.*;

import java.util.ArrayList;
import java.util.List;


/**
 * Class representing an Ally in the game
 *
 * @author Ashi Dhandia
 */
public class Ally extends Actor {

    /**
     * list of behaviours for Ally
     */
    public List<Behaviour> behaviours = new ArrayList<>();

    /**
     * Constructor for Ally
     *
     * @param startingHP     starting hit points for Ally
     * @param startingWeapon starting weapon for Ally
     */
    public Ally(int startingHP, WeaponItem startingWeapon) {
        super("Ally", 'A', startingHP);
        this.addCapability(Status.ALLY);
        this.addWeaponToInventory(startingWeapon);
        this.behaviours.add(new AttackBehaviour());
        this.behaviours.add(new WanderBehaviour());
    }

    /**
     * Plays a turn for this Ally by selecting an action from its behaviours
     *
     * @param actions    collection of possible Actions for this Actor
     * @param lastAction the Action this Actor took last turn, can do interesting things in conjunction with Action.getNextAction()
     * @param map        the map containing the Actor
     * @param display    the I/O object to which messages may be written
     * @return an action to be performed by this Ally
     */
    @Override
    public Action playTurn(ActionList actions, Action lastAction, GameMap map, Display display) {
        for (Behaviour behaviour : behaviours) {
            Action action = behaviour.getAction(this, map);
            if (action != null) {
                return action;
            }
        }
        return new DoNothingAction();
    }


    /**
     * The ally can be attacked by any actor that do not have same status
     * The ally can not be attacked by player
     *
     * @param otherActor the Actor that might be performing attack
     * @param direction  string representing the direction of the other Actor
     * @param map        current GameMap
     * @return the allowable actions that the actor that try to attack can take
     */
    @Override
    public ActionList allowableActions(Actor otherActor, String direction, GameMap map) {
        ActionList actions = super.allowableActions(otherActor, direction, map);
        // for all enemies
        if (!otherActor.hasCapability(Status.HOSTILE_TO_ENEMY) & (otherActor.hasCapability(Status.ALLY) != this.hasCapability(Status.ALLY))) {
            // for area attack action
            for (WeaponItem weaponItem : otherActor.getWeaponInventory()) {
                if (weaponItem.hasCapability(Status.HOSTILE_TO_ALL_ENEMY)) {
                    actions.add(new AreaAttackAction(weaponItem));
                }
            }
            if (otherActor.hasCapability(Status.HOSTILE_TO_ALL_ENEMY)) {
                actions.add(new AreaAttackAction());
            }

            // for attack action
            if (otherActor.getIntrinsicWeapon() != null ) {
                actions.add(new AttackAction(this, direction));
            }
            for (WeaponItem weaponItem : otherActor.getWeaponInventory()) {
                actions.add(new AttackAction(this, direction, weaponItem));
            }
        }
        return actions;
    }
}
