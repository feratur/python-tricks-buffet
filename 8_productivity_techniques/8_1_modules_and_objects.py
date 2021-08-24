#!/usr/bin/env python3
if __name__ == '__main__':
    import datetime
    # alphabetized list of the names and attributes the module provides
    dir(datetime)
    # ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__',
    # '__doc__', '__file__', '__loader__', '__name__',
    # '__package__', '__spec__', '_divide_and_round',
    # 'date', 'datetime', 'datetime_CAPI', 'time',
    # 'timedelta', 'timezone', 'tzinfo']

    dir(datetime.date)
    # ['__add__', '__class__', ..., 'day', 'fromordinal',
    # 'isocalendar', 'isoformat', 'isoweekday', 'max',
    # 'min', 'month', 'replace', 'resolution', 'strftime',
    # 'timetuple', 'today', 'toordinal', 'weekday', 'year']

    # can use filtering
    [_ for _ in dir(datetime) if 'date' in _.lower()]
    # ['date', 'datetime', 'datetime_CAPI']

    # Browse the auto-generated documentation for any Python object:
    # The Python interpreter automatically generates this documentation
    # from the attributes on an object and its docstring (if available.)
    help(datetime)
    # Help on module datetime:

    # NAME
    #     datetime - Fast implementation of the datetime type.
    # CLASSES
    #     builtins.object
    #         date
    #             datetime
    # time
