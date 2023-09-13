package game.actors;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.RandomNumberGenerator;
import game.Status;
import game.actions.AreaAttackAction;
import game.actions.AttackAction;
import game.actions.QuickstepAction;
import game.actions.UnsheatheAction;
import game.behaviours.AttackBehaviour;
import game.behaviours.Behaviour;
import game.behaviours.FollowBehaviour;
import game.behaviours.WanderBehaviour;

import java.util.ArrayList;
import java.util.List;


/**
 * Class representing an Invader in the game
 *
 * @author Ashi Dhandia
 */
public class Invader extends Actor {

    /**
     * player to be followed
     */
    Player player;

    /**
     * list of behaviours for Invader
     */
    public List<Behaviour> behaviours = new ArrayList<>();

    /**
     * Constructor for Invader
     *
     * @param startingHP     starting hit points for Invader
     * @param startingWeapon starting weapon for Invader
     */
    public Invader(int startingHP, WeaponItem startingWeapon) {
        super("Invader", 'ඞ', startingHP);
        this.addCapability(Status.INVADER);
        this.addWeaponToInventory(startingWeapon);
        this.behaviours.add(new FollowBehaviour(player));
        this.behaviours.add(new AttackBehaviour());
        this.behaviours.add(new WanderBehaviour());
    }

    /**
     * Plays a turn for this Invader by selecting an action from its behaviours
     *
     * @param actions    collection of possible Actions for this Actor
     * @param lastAction the Action this Actor took last turn, can do interesting things in conjunction with Action.getNextAction()
     * @param map        the map containing the Actor
     * @param display    the I/O object to which messages may be written
     * @return an action to be performed by this Invader
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
     * Returns a list of allowable actions for another actor to perform on this Invader
     *
     * @param otherActor the Actor that might be performing attack
     * @param direction  string representing the direction of the other Actor
     * @param map        current GameMap
     * @return a list of allowable actions
     */
    @Override
    public ActionList allowableActions(Actor otherActor, String direction, GameMap map) {
        ActionList actions = super.allowableActions(otherActor, direction, map);
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

        if (otherActor.hasCapability(Status.INVADER) != this.hasCapability(Status.INVADER)) {
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
     * Calculates a random number of runes to grant player in case player defeats invader
     *
     * @return a random number of runes between 1358 and 5578 inclusive
     */
    public int runesCalculated() {
        return RandomNumberGenerator.getRandomInt(1358,5578);
    }
}
