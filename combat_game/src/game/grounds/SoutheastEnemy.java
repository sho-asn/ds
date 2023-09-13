package game.grounds;

import edu.monash.fit2099.engine.positions.Location;
import game.RandomNumberGenerator;
import game.actors.fire.FireBird;
import game.actors.stormveil.Dog;
import game.actors.stormveil.GodrickSoldier;
import game.actors.land.SkeletalBandit;
import game.actors.ocean.GiantCrayfish;
import game.actors.wind.GiantDog;

/**
 * This class represents the SoutheastEnemy, that decides what enemies to spawn on the Southeast side of the map
 * @author Seah Thern Fong
 */
public class SoutheastEnemy implements EnemyFactory {
    /**
     * these methods will be the ones that create the types of enemies, and will take in a parameter location to determine what spawns
     * @param location this is the parameter which will be taken into account to determine what spawns
     */
    @Override
    public void CreateOcean(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 1) {
            location.addActor(new GiantCrayfish());
        }
    }

    @Override
    public void CreateLand(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 27) {
            location.addActor(new SkeletalBandit());
        }
    }

    @Override
    public void CreateWind(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 4) {
            location.addActor(new GiantDog());
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
        if (RandomNumberGenerator.getRandomInt(100) <= 45) {
            location.addActor(new GodrickSoldier());
        }
    }

    @Override
    public void CreateFire(Location location) {
        if (RandomNumberGenerator.getRandomInt(100) <= 22) {
            location.addActor(new FireBird());
        }
    }
}
