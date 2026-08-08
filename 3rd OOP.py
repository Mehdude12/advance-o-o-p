class pair_elements:
    def two_sum(self, nums, target):
        look_up = {}
        for i, num in enumerate(nums):
            if target - num in look_up:
                return (look_up[target - num], i)
            look_up[num] = i


value = int(input("Please enter the value of sum: "))
print("index1=%d, index2=%d" % pair_elements().two_sum(
    (10, 20, 30, 40, 50, 60, 70), value))
