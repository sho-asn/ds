package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.RandomNumberGenerator;
import game.Status;


/**
 * Class representing an Unsheathe action
 *
 * @author Ashi Dhandia
 */
public class UnsheatheAction extends Action {

    /**
     * The target actor for the Unsheathe action
     */
    private final Actor target;

    /**
     * The weapon item used for the Unsheathe action
     */
    private final WeaponItem weaponItem;

    /**
     * Constructor for UnsheatheAction
     *
     * @param target     the target actor
     * @param weaponItem the weapon item used to perform this action
     */
    public UnsheatheAction(Actor target, WeaponItem weaponItem) {
        this.target = target;
        this.weaponItem = weaponItem;
    }

    /**
     * Executes the UnsheatheAction.
     * The actor deals 2x damage to the target with a 60% hit rate
     *
     * @param actor the actor performing the action
     * @param map   the map the actor is on
     * @return a string describing the result of the action
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        if (weaponItem.hasCapability(Status.UCHIGATANA)) {
            if (RandomNumberGenerator.getRandomInt(100) <= 60) {
                int damage = weaponItem.damage() * 2;
                target.hurt(damage);
                return actor + " performs Unsheathe and " + weaponItem.verb() + " " + target + " for " +
                        damage + " damage.";
            } else {
                return actor + " fails to perform Unsheathe and misses " + target + ".";
            }
        } else {
            return "Error: Cannot perform Unsheathe with " + weaponItem + ".";
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
        return actor + " unsheathes " + weaponItem + " at " + target;
    }
}
