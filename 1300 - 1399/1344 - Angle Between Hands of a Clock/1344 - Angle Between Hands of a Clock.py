class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:  # 86.78% 46.22%
        if hour == 12:
            hour = 0
        h_hand = 30 * (hour +  minutes / 60)
        m_hand = 6 * minutes
        diff = abs(h_hand - m_hand)
        return diff if diff < 180 else 360 - diff

    def angleClock_best_speed(self, hour: int, minutes: int) -> float:
        min_angle = minutes*6
        hour_add = minutes/60
        
        hour_angle = (hour % 12 + hour_add) * 30
        diff = abs(hour_angle - min_angle)
        
        return min(diff, 360 - diff)
