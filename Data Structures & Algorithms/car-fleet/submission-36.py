class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # by position desc
        print(cars)
        fleets = 0
        cur_time = -1.0

        for pos, spd in cars:
            #從最前面那台車開始看，看他幾秒之後到終點，因為第一台車一定會形成一個fleet所以初始值會是cur_time=t
            #第二台車如果使用的時間比第一台少，就會撞上去，fleet +1，cur_time不變(pass)掉
            # 反而是用加法（我原本是減法）
            # 我卡住的點比較像是這裡敘述邏輯不好
            t = (target - pos) / spd
            if t > cur_time:
                fleets += 1
                cur_time = t
        return fleets
