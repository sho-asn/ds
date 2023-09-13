package game.grounds;

import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;

/**
 * This class represents a PuddleOfWater, that is a type of environment that will spawn GiantCrab and GiantCrayfish
 * this class is used to spawn enemies in the game map
 * @author Seah Thern Fong
 */
public class PuddleOfWater extends Ground {
    /**
     * these are the attributes that the Barrack class contains, like SouthwestEnemy, SoutheastEnemy, NorthwestEnemy, NortheastEnemy, etc
     */
    private SouthwestEnemy southwestEnemy = new SouthwestEnemy();
    private SoutheastEnemy southeastEnemy = new SoutheastEnemy();
    private NorthwestEnemy northwestEnemy = new NorthwestEnemy();
    private NortheastEnemy northeastEnemy = new NortheastEnemy();
    GameMap gameMap;
    int middleWidth;
    int middleHeight;

    /**
     * Constructor for the PuddleOfWater, this will make sure that the puddle of water will be represented with a letter ~.
     */
    public PuddleOfWater() {
        super('~');
    }

    /**
     * This method is so that the grounds can experience the flow of time, and therefore spawn enemies, after taking in a location
     * @param location The location of the Ground
     */
    public void tick(Location location) {
        gameMap = location.map();
        middleWidth = (gameMap.getXRange().max()) / 2;
        middleHeight = (gameMap.getYRange().max()) / 2;

        if (!location.containsAnActor())
            if (location.x() <= middleWidth && location.y() <= middleHeight) {
                northwestEnemy.CreateOcean(location);
            } else if (location.x() <= middleWidth && location.y() >= middleHeight) {
                southwestEnemy.CreateOcean(location);
            } else if (location.x() >= middleWidth && location.y() <= middleHeight) {
                northeastEnemy.CreateOcean(location);
            } else if (location.x() >= middleWidth && location.y() >= middleHeight) {
                southeastEnemy.CreateOcean(location);
            }
    }
}
