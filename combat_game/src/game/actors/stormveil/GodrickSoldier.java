package game.actors.stormveil;

import game.RandomNumberGenerator;
import game.actors.stormveil.Stormveil;
import game.weapons.HeavyCrossbow;

/**
 * Enemy: This is a class for the Godrick Soldier, one of the enemies in the game
 * @author Seah Thern Fong
 */
public class GodrickSoldier extends Stormveil {

    /**
     * This is the constructor for a Godrick Soldier, and it passes the relevant parameters to create the Godrick Soldier
     */
    public GodrickSoldier() {
        super("Godrick Soldier", 'p', 198);
        this.addWeaponToInventory(new HeavyCrossbow());
    }

    /**
     * This is used to randomly generate the runes after the player kills the Dog
     * @return dropped runes
     */
    @Override
    public int droppedRunes() {
        return RandomNumberGenerator.getRandomInt(38, 70);
    }

    @Override
    public void reset() {

    }
}

