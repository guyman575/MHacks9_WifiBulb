import datetime
import time



#TODO Return a hex value as a string for the color based on the time of day
#NOTE: Format of collors are RRGGBBWW, if a value other than 00 is assigned to WW
#       Then the bulb will only show white. I think that ff is full brightness and 00
#       is off. You should use values like 000000ff. See speed_color.py for example
#       on having a range of values. or do it your own way.




def check_time():
    time_epoch = time.time()
    
    
    
    time_day = datetime.datetime.fromtimestamp(time_epoch).strftime( '%H:%M:%S')
    
    time_day_string = time_day.split(":")
    
    time_dayint = int(time_day_string[0] + time_day_string[1] + time_day_string[2])
    
    time_dayint
    bed_time = '1:30:00'
    bed_time = bed_time.split(":")
    
    bed_timeint = int(bed_time[0] + bed_time[1] + bed_time[2])
    
    wake_time = '7:00:00'
    wake_time = wake_time.split(":")
    wake_timeint = int(wake_time[0] + wake_time[1] + wake_time[2])
    
    
    fluid_color = '00000000'
    noon_secs = 43200
    joes_var = float(255/86400)
    
    
    if time_dayint >= bed_timeint and time_dayint <= wake_timeint:
        fluid_color = '00000000'
    else:
        hours = int(time_day_string[0])
        minutes = int(time_day_string[1])
        seconds = int(time_day_string[2])
        secs = 3600*hours + 60*minutes + seconds
        print secs
        time_frm_noon = abs(noon_secs - secs)
        print time_frm_noon
        dec_val = 255 - time_frm_noon*(joes_var)
        print dec_val
        fluid_color = rgb_to_hex(255,255, dec_val)
        print fluid_color
    
    return fluid_color

def rgb_to_hex(red, green, blue):
    
    return '#%02x%02x%02x' % (red, green, blue)


if __name__ == '__main__':
    check_time()

#def subtract_dec():
