package game.actors.ocean;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;


/**
 * Enemy: Giant Crab
 * @author Shosuke Asano
 *
 */
public class GiantCrab extends Ocean {

    /**
     * The constructor for Giant Crab
     */
    public GiantCrab() {
        super("Giant Crab", 'C', 407);
    }

    /**
     * Intrinsic weapon is created
     *
     * @return Intrinsic weapon for this enemy
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(208, "hits", 90);
    }

    /**
     * Randomly generate the runes after death
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(318,4961);
    }

    @Override
    public void reset() {
    }
}

