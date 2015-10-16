#!/usr/bin/env python
from uvaclient import uvaclient
import sys
import urllib2
import os

class command():
    def __init__(self, func, h):
        self.func = func
        self.h = h

    def __call__(self, *args):
        self.func(*args)

def sub_command(client, args):
    if (len(args) > 0):
        client.submissions(args[0])
    else:
        client.submissions()

def submit_command(client, args):
    print "Logging in..."
    client.login()
    print "Submitting..."
    client.submit(args[0], args[1], args[2])
    print "Done!"

def display_command(client, args):
    response = urllib2.urlopen("https://uva.onlinejudge.org/external/" + str(int(args[0])/100) + "/" + args[0] + ".pdf")
    file = open(args[0] + ".pdf", 'w')
    file.write(response.read())
    file.close()
    os.system("open " + args[0] + ".pdf")


if __name__ == "__main__":
    commands = {
        "subs": command(sub_command, "Usage: uva subs [n]"),
        "submit": command(submit_command, "Usage: uva submit <problem_number> <language_option> <source_file>"),
        "display": command(display_command, "Usage: uva problem <problem_number>")
    }

    command = sys.argv[1]
    sys.argv = sys.argv[2:]

    if command in commands:
        u = uvaclient()
        commands[command](u, sys.argv)

    else:
        print "Commands:"
        for name in commands.keys():
            print "\t" + name + " - " + commands[name].h
