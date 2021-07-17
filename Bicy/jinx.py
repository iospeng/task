class jinx:
    hero_hp = 1000
    hero_power = 210

    def fight(self, enemy_hp, enemy_power):
        """

        :param enemy_hp: 敌人的血量，整型
        :param enemy_power: 敌人的攻击力，是整型
        :return:
        """
        # 计算英雄的最终血量
        hero_ffinal_hp = self.hero_hp - enemy_power
        # 计算敌人的最终血量
        enemy_final_hp = enemy_hp - self.hero_power
        # 判断谁的血量多
        if hero_ffinal_hp > enemy_final_hp:
            print("jinx赢了")
        elif hero_ffinal_hp < enemy_final_hp:
            print("ez赢了")
        else:
            print("平局")


class Ez:
    hero_hp = 1100
    hero_power = 190
    def fight(self,enemy_hp, enemy_power):
        """

        :param enemy_hp: 敌人的血量，整型
        :param enemy_power: 敌人的攻击力，是整型
        :return:
        """
        # 计算英雄的最终血量
        hero_ffinal_hp = self.hero_hp - enemy_power
        # 计算敌人的最终血量
        enemy_final_hp = enemy_hp - self.hero_power
        # 判断谁的血量多
        if hero_ffinal_hp > enemy_final_hp:
            print("jinx赢了")
        elif hero_ffinal_hp < enemy_final_hp:
            print("ez赢了")
        else:
            print("平局")

j_jink = jinx()
j_jink.fight(Ez.hero_hp, Ez.hero_power)