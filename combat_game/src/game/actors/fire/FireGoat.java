package game.actors.fire;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;

/**
 * Enemy: This is a class for the FireGoat, one of the enemies in the game (Creative Requirement)
 * @author Seah Thern Fong
 */
public class FireGoat extends Fire {

    /**
     * This is the constructor for a FireGoat, and it passes the relevant parameters to create the FireGoat
     */
    public FireGoat() {
        super("FireGoat", 'i', 290);
    }

    /**
     * This is where the intrinsic weapon is created
     *
     * @return Intrinsic weapon for the FireGoat
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(86, "rams", 90);
    }

    /**
     * This is used to randomly generate the runes after the player kills the FireGoat
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(99, 373);
    }

    @Override
    public void reset() {

    }
}

