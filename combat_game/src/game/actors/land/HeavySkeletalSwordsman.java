package game.actors.land;

import game.RandomNumberGenerator;
import game.weapons.Grossmesser;
/**
 * Enemy: Heavy Skeletal Swordsman
 * @author Shosuke Asano
 *
 */
public class HeavySkeletalSwordsman extends Land {

    /**
     * The constructor for Heavy Skeletal Swordsman
     * weapon (Grossmesser) is added
     */
    public HeavySkeletalSwordsman() {
        super("Heavy Skeletal Swordsman", 'q', 153);
        this.addWeaponToInventory(new Grossmesser());
    }


    /**
     * Randomly generate the runes after death
     *
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(35,892);
    }

    @Override
    public void reset() {
    }
}

