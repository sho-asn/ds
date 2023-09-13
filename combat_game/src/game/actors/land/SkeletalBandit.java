package game.actors.land;

import game.RandomNumberGenerator;
import game.weapons.Scimitar;
/**
 * Enemy: Skeletal Bandit
 * @author Shosuke Asano
 *
 */

public class SkeletalBandit extends Land {

    /**
     * The constructor for Skeletal Bandit
     * weapon (Scimitar) is added
     */
    public SkeletalBandit() {
        super("Skeletal Bandit", 'b', 184);
        this.addWeaponToInventory(new Scimitar());
    }

    /**
     * Randomly generate the runes after death
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(35, 892);
    }

    @Override
    public void reset() {
    }
}


