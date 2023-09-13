package game.grounds;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;
import game.Status;
import game.actions.RestAction;

public class SiteOfLostGrace extends Ground {

    /**
     * Constructor
     */
    public SiteOfLostGrace() {
        super('U');
    }

    @Override
    public ActionList allowableActions(Actor actor, Location location, String direction){
        ActionList actions = super.allowableActions(actor, location, direction);
        if (actor.hasCapability(Status.HOSTILE_TO_ENEMY) && location.getGround() == this) {
            actions.add(new RestAction());
        }
        return actions;
    }
}
