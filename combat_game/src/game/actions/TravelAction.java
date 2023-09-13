package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import game.grounds.GoldenFogDoor;

public class TravelAction extends Action {
    private GameMap destination;

    public TravelAction(GameMap destination) {
        this.destination = destination;
    }

    @Override
    public String execute(Actor actor, GameMap map) {
        Location playerLocation = map.locationOf(actor);

        if (playerLocation.getGround() instanceof GoldenFogDoor) {
            map.removeActor(actor);
            map.moveActor(actor, destination.at(playerLocation.x(), playerLocation.y()));
        }
        return actor + " enters the Golden door and travels to another map";
    }
    @Override
    public String menuDescription(Actor actor) {
        return "Enter the Golden Fog Door";
    }
}

