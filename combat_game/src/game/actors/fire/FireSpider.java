package game.actors.fire;

import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.RandomNumberGenerator;

/**
 * Enemy: This is a class for the FireSpider, one of the enemies in the game (Creative Requirement)
 * @author Seah Thern Fong
 */
public class FireSpider extends Fire {

    /**
     * This is the constructor for a FireSpider, and it passes the relevant parameters to create the FireSpider
     */
    public FireSpider() {
        super("FireSpider", 'j', 350);
    }

    /**
     * This is where the intrinsic weapon is created
     *
     * @return Intrinsic weapon for the FireSpider
     */
    public IntrinsicWeapon getIntrinsicWeapon() {
        return new IntrinsicWeapon(69, "webs", 40);
    }

    /**
     * This is used to randomly generate the runes after the player kills the FireSpider
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(100, 490);
    }

    @Override
    public void reset() {

    }
}

