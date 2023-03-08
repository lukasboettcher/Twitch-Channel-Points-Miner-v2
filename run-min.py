from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.entities.Streamer import StreamerSettings

twitch_miner = TwitchChannelPointsMiner(
    username="<name>",
    claim_drops_startup=False,
    enable_analytics=False,
    streamer_settings=StreamerSettings(
        claim_moments=True,
        make_predictions=False,
        follow_raid=True,
        claim_drops=False,
        watch_streak=True,
    )
)

twitch_miner.mine(
    [
        ...
    ],
)