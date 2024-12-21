
package bufmgr;

import java.util.ArrayList;
import java.util.List;

/**
   * class Policy is a subclass of class Replacer use the given replacement
   * policy algorithm for page replacement
   */
class RandomRP extends  Replacer {
//replace Policy above with impemented policy name (e.g., Lru, Clock)

  //
  // Frame State Constants
  //
  protected static final int AVAILABLE = 10;
  protected static final int REFERENCED = 11;
  protected static final int PINNED = 12;

  //Following are the fields required for LRU and MRU policies:
  /**
   * private field
   * An array to hold number of frames in the buffer pool
   */

    private int  frames[];
 
  /**
   * private field
   * number of frames used
   */   
  private int  nframes;

  /** Clock head; required for the default clock algorithm. */
  protected int head;

  /**
   * Class constructor
   * Initializing frames[] pinter = null.
   */
    public RandomRP(BufMgr mgrArg)
    {
      super(mgrArg);
      // initialize the frame states
    for (int i = 0; i < frametab.length; i++) {
      frametab[i].state = AVAILABLE;
    }
      // initialize parameters for LRU and MRU
      nframes = 0;
      frames = new int[frametab.length];

    // initialize the clock head for Clock policy
    head = -1;
    }
  /**
   * Notifies the replacer of a new page.
   */
  public void newPage(FrameDesc fdesc) {
    // no need to update frame state
  }

  /**
   * Notifies the replacer of a free page.
   */
  public void freePage(FrameDesc fdesc) {
    fdesc.state = AVAILABLE;
  }

  /**
   * Notifies the replacer of a pined page.
   */
  public void pinPage(FrameDesc fdesc) {
        
  }

  /**
   * Notifies the replacer of an unpinned page.
   */
  public void unpinPage(FrameDesc fdesc) {

  }
  
  /**
   * Finding a free frame in the buffer pool
   * or choosing a page to replace using your policy
   *
   * @return 	return the frame number
   *		return -1 if failed
   */

  public int pickVictim() {
    if (nframes < frametab.length) {
      // There are free frames, allocate a new one at random
      int newFrame;
      do {
        newFrame = (int) (Math.random() * frametab.length);
      } while (frametab[newFrame].state != AVAILABLE);

      nframes++;
      frames[newFrame] = newFrame;
      frametab[newFrame].state = PINNED;
      return newFrame;
    } else {
      // All frames are used, find an unpinned frame and replace it at random
      List<Integer> unpinnedFrames = new ArrayList<>();
      for (int i = 0; i < nframes; i++) {
        if (frametab[frames[i]].state != PINNED) {
          unpinnedFrames.add(frames[i]);
        }
      }

      if (!unpinnedFrames.isEmpty()) {
        int randomIndex = (int) (Math.random() * unpinnedFrames.size());
        int victimFrame = unpinnedFrames.get(randomIndex);
        return victimFrame;
      } else {
        // If all frames are pinned, return -1 to indicate failure
        return -1;
      }
    }
  }

}

