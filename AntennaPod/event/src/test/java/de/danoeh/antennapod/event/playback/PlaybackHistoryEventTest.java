package de.danoeh.antennapod.event.playback;

import org.junit.Assert;
import org.junit.Test;

public class PlaybackHistoryEventTest {

    @Test
    public void test_playbackHistoryEvent() {
        PlaybackHistoryEvent playbackHistoryEvent = PlaybackHistoryEvent.listUpdated();
        Assert.assertEquals("PlaybackHistoryEvent", playbackHistoryEvent.toString());
    }
}
