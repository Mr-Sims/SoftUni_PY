# v1 - only datetime

from datetime import datetime


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 0
        t = datetime.strptime(f"{self.hours}:{self.minutes}:{self.seconds}", "%H:%M:%S")
        return t.strftime('%H:%M:%S')

    def next_second(self):
        self.seconds += 1
        return self.get_time()

#############################################################
# v2 - datetime & timedelta

from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.t = datetime.strptime(f"{self.hours}:{self.minutes}:{self.seconds}", "%H:%M:%S")

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.t.strftime('%H:%M:%S')

    def next_second(self):
        self.t = self.t + timedelta(seconds=1)
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())



#JUDGE Unittesting

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        t = Time(16, 35, 54)
        self.assertEqual(t.hours, 16)
        self.assertEqual(t.minutes, 35)
        self.assertEqual(t.seconds, 54)

    def test_class_attributes(self):
        self.assertEqual(Time.max_hours, 23)
        self.assertEqual(Time.max_minutes, 59)
        self.assertEqual(Time.max_seconds, 59)

    def test_set_time(self):
        t = Time(1, 2, 3)
        t.set_time(3, 2, 1)
        self.assertEqual(t.hours, 3)
        self.assertEqual(t.minutes, 2)
        self.assertEqual(t.seconds, 1)

    def test_get_time(self):
        t = Time(1, 20, 30)
        res = t.get_time()
        self.assertEqual(res, "01:20:30")

    def test_next_second_no_overflow(self):
        t = Time(1, 20, 30)
        res = t.next_second()
        self.assertEqual(res, "01:20:31")

    def test_next_second_minutes_overflow(self):
        t = Time(1, 59, 59)
        res = t.next_second()
        self.assertEqual(res, "02:00:00")

    def test_next_second_hours_overflow(self):
        t = Time(23, 59, 59)
        res = t.next_second()
        self.assertEqual(res, "00:00:00")

    def test_next_second(self):
        t = Time(0, 0, 0)
        res = t.next_second()
        self.assertEqual(res, "00:00:01")


if __name__ == "__main__":
    unittest.main()