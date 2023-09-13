package game.actors.wind;

import game.RandomNumberGenerator;
import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.actors.Enemy;

/**
 * BEHOLD, DOG!
 * Created by:
 * @author Adrian Kristanto
 * Modified by: Shosuke Asano
 *
 */
public class LoneWolf extends Enemy {

    /**
     * The constructor for Lone Wolf
     *
     */
    public LoneWolf() {
        super("Lone Wolf", 'h', 102);
    }

    /**
     * Intrinsic weapon is created
     *
     * @return Intrinsic weapon for this enemy
     */
    @Override
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(97, "bites", 95);
    }

    /**
     * Randomly generate the runes after death
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(55,1470);
    }

    @Override
    public void reset() {
    }
}
