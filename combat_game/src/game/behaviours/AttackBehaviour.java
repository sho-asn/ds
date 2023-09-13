package game.behaviours;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import game.RandomNumberGenerator;
import game.Status;
import game.actions.AreaAttackAction;
import game.actions.AttackAction;

import java.util.ArrayList;


/**
 * Class for attack behaviour
 *
 * @author Shosuke Asano
 * Modified By: Shosuke Asano and Ashi Dhandia
 */
public class AttackBehaviour implements Behaviour {

    /**
     * Constructor for AttackBehavior
     */
    public AttackBehaviour() {
    }

    /**
     * Based on the actor that are near the actor, the attack action that the actor can perform is returned
     *
     * @param actor the Actor acting
     * @param map the GameMap containing the Actor
     * @return attack action that the actor can perform
     */
    @Override
    public Action getAction(Actor actor, GameMap map) {
        ArrayList<Location> locations = new ArrayList<>();
        boolean isPlayer = false;
        Location playerLocation = null;
        for (Exit exit: map.locationOf(actor).getExits()) {
            Location destination = exit.getDestination();
            if (destination.containsAnActor()) {
                if (destination.getActor().hasCapability(Status.HOSTILE_TO_ENEMY)) {
                    isPlayer = true;
                    playerLocation = destination;
                    break;
                } else {
                    locations.add(destination);
                }
            }
        }
        // if enemy finds player
        if (isPlayer) {
            // attack with weapon
            if (actor.getIntrinsicWeapon() == null) {
                if (actor.getWeaponInventory().get(0).hasCapability(Status.HOSTILE_TO_ALL_ENEMY) &
                        RandomNumberGenerator.getRandomInt(100) <= 50) {
                    return new AreaAttackAction(actor.getWeaponInventory().get(0));
                } else {
                    return new AttackAction(playerLocation.getActor(), "", actor.getWeaponInventory().get(0));
                }
            }
            // attack with intrinsic weapon
            else {
                if (RandomNumberGenerator.getRandomInt(100) <= 50 & actor.hasCapability(Status.HOSTILE_TO_ALL_ENEMY)) {
                    return new AreaAttackAction();
                } else {
                    return new AttackAction(playerLocation.getActor(), "");
                }
            }
        }
        // if enemy cannot find player
        else if (locations.size() != 0){
            int numOfEnemy = locations.size();
            int target = RandomNumberGenerator.getRandomInt(numOfEnemy);
            Location targetLocation = locations.get(target);
            // attack with weapon
            if (actor.getIntrinsicWeapon() == null) {
                if (actor.getWeaponInventory().get(0).hasCapability(Status.HOSTILE_TO_ALL_ENEMY) &
                        RandomNumberGenerator.getRandomInt(100) <= 50) {
                    return new AreaAttackAction(actor.getWeaponInventory().get(0));
                } else {
                    if (targetLocation.getActor().hasCapability(Status.WIND) != actor.hasCapability(Status.WIND) &
                            targetLocation.getActor().hasCapability(Status.LAND) != actor.hasCapability(Status.LAND) &
                            targetLocation.getActor().hasCapability(Status.OCEAN) != actor.hasCapability(Status.OCEAN) &
                            targetLocation.getActor().hasCapability(Status.STORMVEIL) != actor.hasCapability(Status.STORMVEIL) &
                            targetLocation.getActor().hasCapability(Status.INVADER) != actor.hasCapability(Status.INVADER)) {
                        return new AttackAction(targetLocation.getActor(), "", actor.getWeaponInventory().get(0));
                    } else {
                        return null;
                    }
                }
            }
            // attack with intrinsic weapon
            else {
                if (RandomNumberGenerator.getRandomInt(100) <= 50 & actor.hasCapability(Status.HOSTILE_TO_ALL_ENEMY)) {
                    return new AreaAttackAction();
                } else {
                    if (targetLocation.getActor().hasCapability(Status.WIND) != actor.hasCapability(Status.WIND) &
                            targetLocation.getActor().hasCapability(Status.LAND) != actor.hasCapability(Status.LAND) &
                            targetLocation.getActor().hasCapability(Status.OCEAN) != actor.hasCapability(Status.OCEAN) &
                            targetLocation.getActor().hasCapability(Status.STORMVEIL) != actor.hasCapability(Status.STORMVEIL)) {
                        return new AttackAction(targetLocation.getActor(), "");
                    } else {
                        return null;
                    }
                }
            }
        }
        return null;
    }
}
