def output_minutes_as_hours(orig_minutes):
    hour = float(orig_minutes / 60)
    print("%.1f" %hour)
    
minutes = float(input())
output_minutes_as_hours(minutes)