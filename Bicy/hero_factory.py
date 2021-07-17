from Bicy.Hero import Timo, Jinx


class Herofactory:
    def create_hero(self, hero):
        if hero == "Timo":
            return Timo()
        elif hero == "jink":
            return Jinx()
        else:
            raise Exception("该英雄不在英雄池内")

# if __name__ == '__main__':
#
#     hero_factory = Herofactory()
#     jinx = hero_factory.create_hero("jinx")
#     ez = hero_factory.create_hero("ez")
#     jinx.fight(ez.hero_hp, ez.hero_power)

