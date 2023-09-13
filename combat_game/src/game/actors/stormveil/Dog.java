package game.actors.stormveil;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;

/**
 * Enemy: This is a class for the Dog, one of the enemies in the game
 * @author Seah Thern Fong
 */
public class Dog extends Stormveil {

    /**
     * This is the constructor for a Dog, and it passes the relevant parameters to create the Dog
     */
    public Dog() {
        super("Dog", 'a', 104);
    }

    /**
     * This is where the intrinsic weapon is created
     *
     * @return Intrinsic weapon for the Dog
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(101, "bites", 93);
    }

    /**
     * This is used to randomly generate the runes after the player kills the Dog
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(52, 1390);
    }

    @Override
    public void reset() {

    }
}

