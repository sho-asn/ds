package game.grounds;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;

/**
 * Created by:
 * @author Riordan D. Alfredo
 * Modified by:
 *
 */
public class Wall extends Ground {

	/**
	 * Constructor
	 */
	public Wall() {
		super('#');
	}

	/**
	 * To check if the actor can enter or not. No actor can enter.
	 *
	 * @param actor the Actor to check
	 * @return return false
	 */
	@Override
	public boolean canActorEnter(Actor actor) {
		return false;
	}

	/**
	 * to check if the objects can be thrown the block or not. The object can be thrown the block.
	 *
	 * @return return true
	 */
	@Override
	public boolean blocksThrownObjects() {
		return true;
	}
}
