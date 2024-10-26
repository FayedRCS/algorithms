def decayed_followers(intl_followers, fraction_lost_daily, days):
    
    r_rate = 1 - fraction_lost_daily
    
    remaining = intl_followers * (r_rate ** days)

    return remaining
