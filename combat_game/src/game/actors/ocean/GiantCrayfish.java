package game.actors.ocean;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;
import game.actors.Enemy;
/**
 * Enemy: Giant Crayfish
 * @author Shosuke Asano
 *
 */
public class GiantCrayfish extends Enemy {

    /**
     * The constructor for Giant Crayfish
     */
    public GiantCrayfish() {
        super("Giant Crayfish", 'R', 4803);
    }

    /**
     * Intrinsic weapon is created
     *
     * @return Intrinsic weapon for this enemy
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(527, "hits", 100);
    }

    /**
     * Randomly generate the runes after death
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(500, 2374);
    }

    @Override
    public void reset() {
    }
}

