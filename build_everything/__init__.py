import sh
import tempfile
import re
import os
import yaml
import types
import sys


def strings_or_list(o):
    if type(o) in types.StringTypes:
        return [o]
    else:
        assert type(o) == list
        return o

def validate_contains(contains_section):
    assert contains_section.keys() == ['contains']
    for item in strings_or_list(contains_section['contains']):
        if os.path.exists(item):
            return True
    return False

def execute_rules():
    data = yaml.load('rules.yaml')
    for rule in data:
        name = rule.keys()[0]
        print "trying", name
        contains = rule[name][0]
        if validate_contains(contains):
            print "Whoa, we found a match"


def build_one(git_url, project_name):
    project_name_sanitized = re.sub(r'[^a-zA-Z]', '', project_name)

    tmp_dir_name = tempfile.mkdtemp(
        prefix='build_' + project_name_sanitized,
        dir='.')

    sh.git('clone', git_url, tmp_dir_name)
    os.chdir(tmp_dir_name)
    execute_rules()

def build_one_main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    git_url, project_name = argv

    build_one(git_url, project_name)
