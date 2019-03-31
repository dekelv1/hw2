class Time:
    """ Represents the time of the day. """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        if self.hour == 24:
            self.hour = 0
        if isinstance(self.hour, float) or isinstance(self.hour, str):
            print("Error hour, please insert integer from 0 to 24")
            self.hour = None
        elif self.hour < 0 or self.hour > 24:
            self.hour = 0 
        if isinstance(self.minute, float) or isinstance(self.minute, str):
            print("Error minute, please insert integer from 0 to 59")
            self.minute = None
        elif self.minute < 0 or self.minute > 59:
            self.minute = 0
        if isinstance(self.second, float) or isinstance(self.second, str):
            print("Error second, please insert integer from 0 to 59")
            self.minute = None
        elif self.second < 0 or self.second > 59:
            self.second = 0      

    def __str__(self):
        if self.hour == None or self.minute == None or self.second == None:
            str_to_print = f""" """ 
        else:     
            if self.hour < 10:
                str_to_print = f"""The time is: 0{self.hour}:{self.minute}:{self.second}
                """
            if self.minute < 10:
                str_to_print = f"""The time is: {self.hour}:0{self.minute}:{self.second}
                """
            if self.second < 10:
                str_to_print = f"""The time is: {self.hour}:{self.minute}:0{self.second}
                """
            if self.hour < 10 and self.minute < 10:
                str_to_print = f"""The time is: 0{self.hour}:0{self.minute}:{self.second}
                """
            if self.hour < 10 and self.second < 10:
                str_to_print = f"""The time is: 0{self.hour}:{self.minute}:0{self.second}
                """
            if self.minute < 10 and self.second < 10:
                str_to_print = f"""The time is: {self.hour}:0{self.minute}:0{self.second}
                """
            if self.hour < 10 and self.minute < 10 and self.second < 10:
                str_to_print = f"""The time is: 0{self.hour}:0{self.minute}:0{self.second}
                """
            if self.hour > 9 and self.minute > 9 and self.second > 9:            
                str_to_print = f"""The time is: {self.hour}:{self.minute}:{self.second}
                """
        return str_to_print

    def is_after(self,other):
        if self.hour == other.hour and self.minute == other.minute and self.second == other.second:
            return False
        else:
            if self.hour > other.hour:
                return True
            elif self.hour == other.hour:
                if self.minute > other.minute:
                    return True
                elif self.minute == other.minute:
                    if self.second > other.second:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def __add__(self,other): 
        new_hour = self.hour + other.hour
        new_minute = self.minute + other.minute
        new_second = self.second + other.second
        if new_hour < 60 and new_minute < 60 and new_second < 24:
            t_new = Time(new_hour,new_minute,new_second)
        else:
            if new_second >= 60:
                t_new = Time(new_hour, new_minute+1, new_second-60)
                if new_minute+1>=60:
                    t_new = Time(new_hour+1,new_minute-59,new_second-60)
            if new_minute >= 60:
                t_new = Time(new_hour+1, new_minute-60, new_second)
            if new_hour >= 24:
                t_new = Time(new_hour-24, new_minute, new_second)
            if new_second >= 60 and new_minute >= 60:
                t_new = Time(new_hour+1, new_minute-59, new_second-60)
            if new_hour >= 24 and new_minute >= 60:
                t_new = Time(new_hour-23, new_minute-60, new_second)
            if new_hour >= 24 and new_second >= 60:
                t_new = Time(new_hour-24, new_minute+1, new_second-60)
            if new_hour >= 24 and new_second >= 60 and new_minute >= 60:
                t_new = Time(new_hour-23, new_minute-59, new_second-60)

        return t_new
    





