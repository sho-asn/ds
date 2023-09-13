package game;

import java.util.Random;

/**
 * A random number generator
 * Created by:
 * @author Adrian Kristanto
 * Modified by:
 *
 */
public class RandomNumberGenerator {
    /**
     * Generate the number randomly
     * @param bound the upper bound
     * @return random number from 0 to upper bound(exclusive)
     */
    public static int getRandomInt(int bound) {
        return bound > 0 ? new Random().nextInt(bound) : 0;
    }

    /**
     * Generate the number randomly
     * @param lowerBound the lower bound
     * @param upperBound the upper bound
     * @return random number from lower bound to upper bound(exclusive)
     */
    public static int getRandomInt(int lowerBound, int upperBound) {
        int range = upperBound - lowerBound + 1;
        return new Random().nextInt(range) + lowerBound;
    }
}
