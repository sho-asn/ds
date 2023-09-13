package game.grounds;

import edu.monash.fit2099.engine.positions.Location;

/**
 * This is an interface "EnemyFactory", this interface will provide methods for spawning enemies on the game map.
 * @author Seah Thern Fong
 */

public interface EnemyFactory {
    /**
     * These methods will spawn an enemy on the game map, on the specific locations and parts of the map
     */
    void CreateOcean(Location location);
    void CreateLand(Location location);
    void CreateWind(Location location);
    void CreateStormveilDog(Location location);
    void CreateSoldier(Location location);
    void CreateFire(Location location);
}

