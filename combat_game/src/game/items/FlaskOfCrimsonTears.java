package game.items;

import edu.monash.fit2099.engine.items.Item;
import game.actions.Consumable;
import game.actions.ConsumeAction;
import game.actors.Player;
import game.reset.Resettable;

/**
 * This FlaskOfCrimsonTears is a class that extends the item class, and implements Consumable
 * This is a class for an item that can be used to heal the player's health by 250 hit points
 * @author Seah Thern Fong
 */
public class FlaskOfCrimsonTears extends Item implements Consumable, Resettable {
    private int numOfUses;
    private final int maxNumOfUses;

    /**
     * Constructor for the FlaskOfCrimsonTears, this will make sure that the flask of crimson tears name will be correct, give its display character
     * this sets the numofUses to 0, and maxNumOfUses, which is final for now, to be 2
     * this adds a ConsumeAction to consume a FlaskOfCrimsonTears to the player's action list, and in the menu description
     * @author Seah Thern Fong
     */
    public FlaskOfCrimsonTears() {
        super("Flask Of Crimson Tears", 'F', false);
        numOfUses = 0;
        maxNumOfUses = 2;
        this.addAction(new ConsumeAction(this));
    }

    /**
     * This method returns the numOfUses
     * @return int type numOfUses
     */
    public int getNumOfUses() {
        return numOfUses;
    }

    /**
     * This method returns the maxNumOfUses
     * @return int type maxNumOfUses
     */
    public int getMaxNumOfUses() {
        return maxNumOfUses;
    }

    /**
     * This method returns a boolean value, to tell whether the FlaskOfCrimsonTears has remaining uses left remaining
     * @return boolean value "valid"
     */
    public boolean hasRemainingUses() {
        boolean valid = true;
        if ((numOfUses == maxNumOfUses)) {
            valid = false;
            System.out.println("Flask of Crimson Tears (" + (getMaxNumOfUses()-getNumOfUses()) + "/" + getMaxNumOfUses() + ") is empty.");
        }
        return valid;
    }

    /**
     * This method is used to be able to heal the player's hit points by 250
     * @param player this variable is used, so that the player's hit points will be restored by 250
     */
    public void heal(Player player) {
        if (hasRemainingUses()) {
            player.heal(250);
        }
    }

    /**
     * This method is used to consume the FlaskOfCrimsonTears
     * the numOfUses will increment by 1
     */
    @Override
    public void consume(Player actor) {
        if (this.hasRemainingUses()) {
            numOfUses++;
            this.heal(actor);
            numOfUses++;
        }
    }

    @Override
    public void reset() {
        numOfUses = 0;
    }
}


