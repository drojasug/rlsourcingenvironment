from gym.envs.registration import register

register(
    id='gym-sourcing-v0',
    entry_point='gym_sourcing.envs:SourcingEnv',
)