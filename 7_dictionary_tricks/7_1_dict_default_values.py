#!/usr/bin/env python3
if __name__ == '__main__':
    name_for_userid = {
        382: 'Alice',
        950: 'Bob',
        590: 'Dilbert',
    }
    def greeting(userid):
        if userid in name_for_userid:
            return 'Hi %s!' % name_for_userid[userid]
        else:
            return 'Hi there!'
    # It’s inefficient because it queries the dictionary twice.
    # It’s verbose since part of the greeting string is repeated, for example.
    # It’s not Pythonic—the official Python documentation specifically recommends
    # an “easier to ask for forgiveness than permission” (EAFP) coding style
    def greeting_shorter(userid):
        try:
            return 'Hi %s!' % name_for_userid[userid]
        except KeyError:
            return 'Hi there'
    # But there is a cleaner solution
    def greeting_shortest(userid):
        return 'Hi %s!' % name_for_userid.get(userid, 'there')

    # Avoid explicit key in dict checks when testing for membership.
    #
    # EAFP-style exception handling or using the built-in get() method is preferable.
    #
    # In some cases, the collections.defaultdict class from the standard library can also be helpful.
