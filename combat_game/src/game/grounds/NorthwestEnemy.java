package game.grounds;

import edu.monash.fit2099.engine.positions.Location;
import game.RandomNumberGenerator;
import game.actors.fire.FireSpider;
import game.actors.stormveil.Dog;
import game.actors.stormveil.GodrickSoldier;
import game.actors.land.HeavySkeletalSwordsman;
import game.actors.ocean.GiantCrab;
import game.actors.wind.LoneWolf;

/**
 * This class represents the NorthwestEnemy, that decides what enemies to spawn on the Northwest side of the map
 * @author Seah Thern Fong
 */
public class NorthwestEnemy implements EnemyFactory {
    /**
     * these methods will be the ones that create the types of enemies, and will take in a parameter location to determine what spawns
     * @param location this is the parameter which will be taken into account to determine what spawns
     */
    @Override
    public void CreateOcean(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 2) {
            location.addActor(new GiantCrab());
        }
    }

    @Override
    public void CreateLand(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 27) {
            location.addActor(new HeavySkeletalSwordsman());
        }
    }

    @Override
    public void CreateWind(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 33) {
            location.addActor(new LoneWolf());
        }
    }

    @Override
    public void CreateStormveilDog(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 37) {
            location.addActor(new Dog());
        }
    }

    @Override
    public void CreateSoldier(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 45 ) {
            location.addActor(new GodrickSoldier());
        }
    }

    @Override
    public void CreateFire(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 29) {
            location.addActor(new FireSpider());
        }
    }
}
