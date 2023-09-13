package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.RandomNumberGenerator;
import game.Status;

import java.util.ArrayList;
import java.util.List;

/**
 * Class representing a Quickstep action
 *
 * @author Ashi Dhandia
 */
public class QuickstepAction extends Action {

    /**
     * The target actor for the Quickstep action
     */
    private final Actor target;

    /**
     * The weapon item used for the Quickstep action
     */
    private final WeaponItem weaponItem;


    /**
     * Constructor for QuickstepAction
     *
     * @param target     the target actor
     * @param weaponItem the weapon item used to perform this action
     */
    public QuickstepAction(Actor target, WeaponItem weaponItem) {
        this.target = target;
        this.weaponItem = weaponItem;
    }

    /**
     * Executes the Quickstep action.
     * The actor deals normal damage to the target with a 70% hit rate,
     * then moves to a random adjacent location if possible.
     *
     * @param actor the actor performing the action.
     * @param map The map the actor is on.
     * @return a string describing the result of the action
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        // only Great Knife has the ability to perform Quickstep action
        if (weaponItem.hasCapability(Status.GREAT_KNIFE)) {
            // deals normal damage with 70% chance to hit target
            int damage = 0;
            if (RandomNumberGenerator.getRandomInt(100) <= 70) {
                damage = weaponItem.damage();
                target.hurt(damage);
            }
            String result;
            if (damage > 0) {
                result = actor + " deals " + damage + " damage to " + target + ".";
            } else {
                result = actor + " misses the target.";
            }

            // get location of actor
            Location actorLocation = map.locationOf(actor);
            // get all locations within player's surroundings
            List<Exit> adjacentLocations = new ArrayList<>(actorLocation.getExits());
            // remove locations that have actors
            adjacentLocations.removeIf(exit -> exit.getDestination().containsAnActor());
            if (!adjacentLocations.isEmpty()) {
                // choose a random adjacent location
                Exit chosenExit = adjacentLocations.get(RandomNumberGenerator.getRandomInt(adjacentLocations.size()));
                Location newLocation = chosenExit.getDestination();
                if (newLocation.canActorEnter(actor)) {
                    map.moveActor(actor, newLocation);
                    return result + (System.lineSeparator() + actor + " moves to " + newLocation + ".");
                } else {
                    return result + (System.lineSeparator() + actor + " was unable to perform Quickstep!");
                }
            } else {
                return result + (System.lineSeparator() + actor + " was unable to perform Quickstep!");
            }
        } else {
            return "Error: Cannot perform Quickstep with " + weaponItem + ".";
        }
    }

    /**
     * Returns a description of this action for display in menu
     *
     * @param actor the actor performing the action
     * @return a description used for the menu UI
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " performs Quickstep on " + target;
    }
}
