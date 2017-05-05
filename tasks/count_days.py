from datetime import date

def count_days(d1, d2):
    # Baby, lately I've been lossing sleep, dreaming about
    # the things that we could be...
    # But baby lately I've been praying hard, so no more
    # counting dollars, we'll be counting days...
    different_days = d2 - d1
    # Check if date d1 is newer than d2
    if different_days.days < 0:
        raise ValueError
    return different_days
