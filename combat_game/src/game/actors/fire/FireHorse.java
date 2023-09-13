package game.actors.fire;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;

/**
 * Enemy: This is a class for the FireHorse, one of the enemies in the game (Creative Requirement)
 * @author Seah Thern Fong
 */
public class FireHorse extends Fire {

    /**
     * This is the constructor for a FireHorse, and it passes the relevant parameters to create the FireHorse
     */
    public FireHorse() {
        super("FireHorse", 'd', 300);
    }

    /**
     * This is where the intrinsic weapon is created
     *
     * @return Intrinsic weapon for the FireHorse
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(73, "stomps", 70);
    }

    /**
     * This is used to randomly generate the runes after the player kills the FireHorse
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(67, 244);
    }

    @Override
    public void reset() {

    }
}

