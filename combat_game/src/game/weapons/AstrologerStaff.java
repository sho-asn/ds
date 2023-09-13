package game.weapons;

import edu.monash.fit2099.engine.weapons.WeaponItem;

/**
 * Class representing Astrologer's weapon, Astrologer's Staff
 *
 * @author Ashi Dhandia
 */
public class AstrologerStaff extends WeaponItem {

    /**
     * The purchase price of the Astrologer's Staff
     */
    private final int PURCHASE_PRICE = 800;

    /**
     * The selling price of the Astrologer's Staff
     */
    private final int SELL_PRICE = 100;

    /**
     * Constructor for AstrologerStaff
     */
    public AstrologerStaff() {
        super("Astrologer's Staff", 'f', 274, "shoots", 50);
    }

    /**
     * Returns the purchase price of the Astrologer's Staff
     *
     * @return the purchase price of the Astrologer's Staff
     */
    public int getPURCHASE_PRICE() {
        return PURCHASE_PRICE;
    }

    /**
     * Returns the selling price of the Astrologer's Staff
     *
     * @return the selling price of the Astrologer's Staff
     */
    public int getSELL_PRICE() {
        return SELL_PRICE;
    }
}
