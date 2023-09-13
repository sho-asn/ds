package game.grounds;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;
import game.actors.Player;

/**
 * This class represents a Cliff, that is a type of environment that will kill the player if they step on it
 * @author Seah Thern Fong
 */
public class Cliff extends Ground {
    /**
     * Constructor for the Cliff, this will make sure that the cliff will be represented with a symbol + .
     *
     * @author Seah Thern Fong
     */
    public Cliff() {
        super('+');
    }

    @Override
    public boolean canActorEnter(Actor actor) {
        boolean isTrue = false;
        if (actor instanceof Player) {
            isTrue = true;
        }
        return isTrue;
    }

}
