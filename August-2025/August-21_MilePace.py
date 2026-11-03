"""
Mile Pace

Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

    Add leading zeros when needed.


"""


def mile_pace(miles, duration):
    minutes, seconds = map(int, duration.split(":"))
    total_Seconds = (minutes * 60) + seconds

    avg_seconds_per_mile = round(total_Seconds / miles)

    pace_minutes = avg_seconds_per_mile // 60
    pace_seconds = avg_seconds_per_mile % 60

    return f"{pace_minutes:02d}:{pace_seconds:02d}"


print(mile_pace(3, "24:00"))
