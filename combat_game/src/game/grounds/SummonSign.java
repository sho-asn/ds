package game.grounds;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;
import game.Status;
import game.actions.SummonAction;

/**
 * Class representing Summon Sign ground
 *
 * @author Ashi Dhandia
 */
public class SummonSign extends Ground {

    /**
     * Constructor for SummonSign
     */
    public SummonSign() {
        super('=');
    }

    /**
     * Returns an updated list of allowable actions for player; ability to summon
     * when on/near this ground
     *
     * @param actor the Actor acting
     * @param location the current Location
     * @param direction the direction of the Ground from the Actor
     * @return a list of allowable actions
     */
    @Override
    public ActionList allowableActions(Actor actor, Location location, String direction){
        ActionList actions = super.allowableActions(actor, location, direction);
        if (actor.hasCapability(Status.HOSTILE_TO_ENEMY) && location.getGround() == this) {
            actions.add(new SummonAction(location));
        }
        return actions;
    }
}
