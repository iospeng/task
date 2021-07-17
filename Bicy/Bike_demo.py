class Bike:

    def run(self, miles):
        print(f"人工骑行：{miles}公里")


class Ebike(Bike):
    volume = 10

    def fill_charge(self, vol):

        """
        :param vol: 充电电量
        :return:
        """
        self.volume = self.volume + vol
        print(f"充电之后的电量：{self.volume}")

    def run_e(self, miles):

        # 电量可骑行的里程数
        vol_volum = self.volume * 10
        # 判断电量是否耗尽
        if vol_volum >= miles:
            print(f"自动骑行了{miles}公里")
        else:
            print(f"自动骑行了{vol_volum}")
            # self.run(miles-vol_volum)
            # 使用super重写父类方法
            super().run(miles-vol_volum)

e_ebike = Ebike()

# e_ebike.run(1000)
e_ebike.run_e(1000)