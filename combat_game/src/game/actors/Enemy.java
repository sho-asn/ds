package game.actors;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.*;
import game.actions.*;
import game.actors.Player;
import game.behaviours.*;
import game.reset.Resettable;

import java.util.ArrayList;
import java.util.List;

/**
 * An enemy class
 * @author Adrian Kristanto
 *
 * Modified by: Shosuke Asano
 */
public abstract class Enemy extends Actor implements Resettable {

    /**
     * player to be followed
     */
    Player player;

    /**
     * collection of behaviours for enemy
     */
    public List<Behaviour> behaviours = new ArrayList<>();

    /**
     * Constructor for Enemy
     *
     * @param name        the name of the Actor
     * @param displayChar the character that will represent the Actor in the display
     * @param hitPoints   the Actor's starting hit points
     */
    public Enemy(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.behaviours.add(new FollowBehaviour(player));
        this.behaviours.add(new AttackBehaviour());
        this.behaviours.add(new WanderBehaviour());
    }

    /**
     * At each turn, select a valid action to perform.
     *
     * @param actions    collection of possible Actions for this Actor
     * @param lastAction the Action this Actor took last turn, can do interesting things in conjunction with Action.getNextAction()
     * @param map        the map containing the Actor
     * @param display    the I/O object to which messages may be written
     * @return the valid action that can be performed in that iteration or null if no valid action is found
     */
    @Override
    public Action playTurn(ActionList actions, Action lastAction, GameMap map, Display display) {
        if (RandomNumberGenerator.getRandomInt(100) <= 10) {
            return new Despawn();
        }

        for (Behaviour behaviour : behaviours) {
            Action action = behaviour.getAction(this, map);
            if (action != null) {
                return action;
            }
        }
        return new DoNothingAction();
    }

    /**
     * The enemy can be attacked by a player that has the HOSTILE_TO_ENEMY capability
     * The enemy can be attacked by enemies that has the HOSTILE_TO_ALL_ENEMY capability
     * The enemy can be attacked by any actor that do not have same status
     *
     * @param otherActor the Actor that might be performing attack
     * @param direction  string representing the direction of the other Actor
     * @param map        current GameMap
     * @return the allowable actions that the actor that try to attack can take
     */
    @Override
    public ActionList allowableActions(Actor otherActor, String direction, GameMap map) {
        ActionList actions = super.allowableActions(otherActor, direction, map);
        // for player
        if (otherActor.hasCapability(Status.HOSTILE_TO_ENEMY)) {
            actions.add(new AttackAction(this, direction));
            for (WeaponItem weaponItem : otherActor.getWeaponInventory()) {
                actions.add(new AttackAction(this, direction, weaponItem));
                if (weaponItem.hasCapability(Status.GREAT_KNIFE)) {
                    actions.add(new QuickstepAction(this, weaponItem));
                } else if (weaponItem.hasCapability(Status.UCHIGATANA)) {
                    actions.add(new UnsheatheAction(this, weaponItem));
                }
            }
        }

        for (WeaponItem weaponItem : otherActor.getWeaponInventory()) {
            if (weaponItem.hasCapability(Status.HOSTILE_TO_ALL_ENEMY)) {
                actions.add(new AreaAttackAction(weaponItem));
            }
        }
        if (otherActor.hasCapability(Status.HOSTILE_TO_ALL_ENEMY)) {
            actions.add(new AreaAttackAction());
        }

        if (otherActor.hasCapability(Status.WIND) != this.hasCapability(Status.WIND) &
                otherActor.hasCapability(Status.LAND) != this.hasCapability(Status.LAND) &
                otherActor.hasCapability(Status.OCEAN) != this.hasCapability(Status.OCEAN) &
                otherActor.hasCapability(Status.STORMVEIL) != this.hasCapability(Status.STORMVEIL)) {
            if (otherActor.getIntrinsicWeapon() != null ) {
                actions.add(new AttackAction(this, direction));
            }
            for (WeaponItem weaponItem : otherActor.getWeaponInventory()) {
                actions.add(new AttackAction(this, direction, weaponItem));
            }
        }
        return actions;
    }

    /**
     * Abstract method that returns the number of runes that is dropped after death
     *
     * @return number of dropped runes by enemy
     */
    public abstract int droppedRunes();
}

