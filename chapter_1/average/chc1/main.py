def average_followers(nums):
    average = 0

    if nums == []:
        return None

    for addends in nums:
        average += addends

    average = average / len(nums)

    return average
