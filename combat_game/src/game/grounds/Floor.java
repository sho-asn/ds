package game.grounds;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;
import game.Status;

/**
 * A class that represents the floor inside a building.
 * Created by:
 * @author Riordan D. Alfredo
 * Modified by:
 *
 */
public class Floor extends Ground {
	/**
	 * Constructor
	 */
	public Floor() {
		super('_');
	}

	/**
	 * To check the actor can enter or not. Only player can enter.
	 *
	 * @param actor the Actor to check
	 * @return if actor is player, return true, otherwise false.
	 */
	@Override
	public boolean canActorEnter(Actor actor) {
		return actor.hasCapability(Status.HOSTILE_TO_ENEMY);
	}
}
