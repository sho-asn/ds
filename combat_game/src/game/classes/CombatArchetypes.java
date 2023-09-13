package game.classes;

import edu.monash.fit2099.engine.weapons.WeaponItem;


/**
 * Abstract class representing a combat archetype (role for players) in the game
 *
 * @author Ashi Dhandia
 */
public abstract class CombatArchetypes {

    /**
     * starting weapon for this combat archetype
     */
    private final WeaponItem startingWeapon;

    /**
     * starting hit points for this combat archetype
     */
    private final int startingHP;

    /**
     * Constructor for CombatArchetypes
     *
     * @param startingWeapon starting weapon for this combat archetype
     * @param startingHP     starting hit points for this combat archetype
     */
    public CombatArchetypes(WeaponItem startingWeapon, int startingHP) {
        this.startingWeapon = startingWeapon;
        this.startingHP = startingHP;
    }

    /**
     * Returns the starting weapon for this combat archetype
     *
     * @return the starting weapon
     */
    public WeaponItem getStartingWeapon() {
        return startingWeapon;
    }

    /**
     * Returns the starting hit points for this combat archetype
     *
     * @return the starting hit points
     */
    public int getStartingHP() {
        return startingHP;
    }
}
