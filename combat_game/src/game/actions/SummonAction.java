package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import game.RandomNumberGenerator;
import game.actors.Ally;
import game.actors.Invader;
import game.classes.*;

import java.util.Random;


/**
 * Class representing an action that allows the player to summon an ally or invader
 *
 * @author Ashi Dhandia
 */
public class SummonAction extends Action {

    /**
     * Array of available roles
     */
    private final CombatArchetypes[] availableRoles = {new Astrologer(), new Bandit(), new Samurai(), new Wretch()};

    /**
     * Location of Summon Sign
     */
    private final Location summonSignLocation;

    /**
     * Constructor for SummonAction
     *
     * @param summonSignLocation location of Summon Sign
     */
    public SummonAction(Location summonSignLocation) {
        this.summonSignLocation = summonSignLocation;
    }

    /**
     * Executes the SummonAction by creating an ally or invader and adding it to the game map
     *
     * @param actor the actor performing the action
     * @param map the map the actor is on
     * @return a string describing the outcome of the action
     */
    @Override
    public String execute(Actor actor, GameMap map) {
        Actor summonedActor;
        // 50% chance to create an ally or invader
        if (Math.random() < 0.5) {
            summonedActor = createAlly();
        } else {
            summonedActor = createInvader();
        }
        // find an empty spot adjacent to Summon Sign
        Location emptySpot = findEmptySpot(summonSignLocation, summonedActor);
        if (emptySpot != null) {
            // add the summoned actor (ally/invader) to that location
            emptySpot.addActor(summonedActor);
            return actor + " summons an " + summonedActor.getClass().getSimpleName();
        }
        return "No empty location found to spawn Ally or Invader";
    }

    /**
     * Creates an instance of Ally with a random combat role
     *
     * @return a new instance of Ally
     */
    private Ally createAlly() {
        CombatArchetypes role = getRandomRole();
        return new Ally(role.getStartingHP(), role.getStartingWeapon());
    }

    /**
     * Creates an instance of Invader with a random combat role
     *
     * @return a new instance of Invader
     */
    private Invader createInvader() {
        CombatArchetypes role = getRandomRole();
        return new Invader(role.getStartingHP(), role.getStartingWeapon());
    }

    /**
     * Returns a random combat role from the available roles array
     *
     * @return a random combat role
     */
    private CombatArchetypes getRandomRole() {
        int index = RandomNumberGenerator.getRandomInt(availableRoles.length);
        return availableRoles[index];
    }

    /**
     * Finds and returns the location of an empty spot adjacent to summon sign
     *
     * @param summonSignLocation location of Summon Sign
     * @param summonedActor the actor being summoned
     * @return an empty location adjacent to Summon Sign, or null if none is found
     */
    private Location findEmptySpot(Location summonSignLocation, Actor summonedActor) {
        for (Exit exit : summonSignLocation.getExits()) {
            Location destination = exit.getDestination();
            if (destination.canActorEnter(summonedActor) && destination.getActor() == null) {
                return destination;
            }
        }
        return null;
    }

    /**
     * Returns a description of this action for display in menu
     *
     * @param actor the actor performing the action
     * @return a string describing this action
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " summons Ally or Invader";
    }
}
