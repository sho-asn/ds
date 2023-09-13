package game.actors.fire;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;

/**
 * Enemy: This is a class for the FireBird, one of the enemies in the game (Creative Requirement)
 * @author Seah Thern Fong
 */
public class FireBird extends Fire {

    /**
     * This is the constructor for a FireBird, and it passes the relevant parameters to create the FireBird
     */
    public FireBird() {
        super("FireBird", 'r', 250);
    }

    /**
     * This is where the intrinsic weapon is created
     *
     * @return Intrinsic weapon for the FireBird
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(50, "scratches", 84);
    }

    /**
     * This is used to randomly generate the runes after the player kills the FireBird
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(30, 136);
    }

    @Override
    public void reset() {

    }
}

