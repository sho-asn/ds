package game.grounds;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;
import game.actions.TravelAction;
import game.actors.Player;

/**
 * This class represents a GoldenFogDoor, that is a type of place that will allow the player to move to a different map if they step on it
 * @author Seah Thern Fong
 */
public class GoldenFogDoor extends Ground {
    private GameMap destination;

    /**
     * Constructor for the GoldenFogDoor, this will make sure that the door will be represented with a letter D.
     * @author Seah Thern Fong
     */
    public GoldenFogDoor(GameMap destination) {
        super('D');
        this.destination = destination;
    }

    /**
     * This method is used to check if the player can enter the golden fog door
     * @param actor the Actor to check
     * @return isTrue, a boolean to see if the actor could enter the door or not
     */
    @Override
    public boolean canActorEnter(Actor actor) {
        boolean isTrue = false;
        if (actor instanceof Player) {
            isTrue = true;
        }
        return isTrue;
    }

    /**
     * This method is used to return an action list, based on whether the actor is a player or a non-player
     * @param actor the Actor acting
     * @param location the current Location
     * @param direction the direction of the Ground from the Actor
     * @return an action list that allows the player to travel, like TravelAction, but a DoNothingAction if the actor is not a player
     */
    @Override
    public ActionList allowableActions(Actor actor, Location location, String direction) {
        if (canActorEnter(actor))
            return new ActionList(new TravelAction(destination));
        return new ActionList(new DoNothingAction()); // returns a do nothing action, since only player can use this
    }

}
