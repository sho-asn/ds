package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.Weapon;

/**
 * An Action to attack surrounding Actors.
 * @author Shosuke Asano
 *
 */
public class AreaAttackAction extends Action{
    /**
     * Weapon used for the attack
     */
    private Weapon weapon;

    /**
     * Constructor with weapon item
     * @param weapon the Weapon which is used to attack
     */
    public AreaAttackAction(Weapon weapon) {
        this.weapon = weapon;
    }

    /**
     * Constructor with intrinsic weapon as default
     */
    public AreaAttackAction() {}


    /**
     * When executed, the chance to hit of the weapon that the Actor used is computed to determine whether
     * the actor will hit the surrounding actors. If so, deal damage to the actors and determine whether they are killed.
     *
     * @param actor The actor performing the attack action.
     * @param map The map the actor is on.
     * @return the result of the attack, e.g. whether the actors are killed, etc.
     * @see DeathAction
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        String result = "";
        for (Exit exit : map.locationOf(actor).getExits()) {
            Location destination = exit.getDestination();
            if (destination.containsAnActor()){
                Actor surroundingActor = destination.getActor();
                if (weapon == null) {
                    AttackAction attackWithoutWeaponItem = new AttackAction(surroundingActor, "");
                    result += attackWithoutWeaponItem.execute(actor, map) + "\n";
                } else {
                    AttackAction attackWithWeaponItem = new AttackAction(surroundingActor, "", weapon);
                    result += attackWithWeaponItem.execute(actor, map) + "\n";
                }
            }
        }
        return result;
    }

    /**
     * Describes which target the actor is attacking with which weapon
     * @return a description used for the menu UI
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " conducts area attack " + " with " + (weapon != null ? weapon : "Intrinsic Weapon");
    }
}