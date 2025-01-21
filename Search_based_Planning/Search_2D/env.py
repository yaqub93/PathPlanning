"""
Env 2D
@author: huiming zhou
"""


class Env:
    def __init__(self):
        self.x_range = 1501  # size of background
        self.y_range = 1001
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))


        for i in range(50, 400):
            obs.add((i, 600))
        
        for i in range(450, 1000):
            obs.add((i, 600))
        
        for i in range(1000, 1400):
            obs.add((i, 450))
        
        for i in range(100, 610):
            obs.add((i, 250))
        for i in range(250):
            obs.add((600, i))

        for i in range(250, 850):
            obs.add((1000, i))
        for i in range(360):
            obs.add((1200, i))

        for i in range(250, 950):
            obs.add((400, i))

        #for i in range(75, 100):
        #    obs.add((40, i))

        return obs
