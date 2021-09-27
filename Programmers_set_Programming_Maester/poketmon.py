def solution(nums):
    half = len(nums)//2
    num = set(nums)
    return len(num) if len(num) < half else half
