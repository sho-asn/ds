package game.actors.wind;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;
import game.Status;
import game.actors.Enemy;
/**
 * Enemy: Giant Dog
 * @author Shosuke Asano
 *
 */
public class GiantDog extends Enemy {

    /**
     * The constructor for Giant Dog
     *
     */
    public GiantDog() {
        super("Giant Dog", 'G', 693);
        this.addCapability(Status.HOSTILE_TO_ALL_ENEMY);
    }

    /**
     * Intrinsic weapon is created
     *
     * @return Intrinsic weapon for this enemy
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(314, "bites", 90);
    }

    /**
     * Randomly generate the runes after death
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(313, 1808);
    }

    @Override
    public void reset() {
    }
}
