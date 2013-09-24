import sh
import tempfile
import re
import os
import yaml
import types
import sys
from . import helpers


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

def do_execute(section):
    assert section.keys() == ['execute']
    for item in strings_or_list(
        section['execute']):
        print "executing:", item
        # hacky sh parsing
        splitted = item.split(' ')
        run = sh.Command(splitted[0])
        run(*splitted[1:])

def execute_rules():
    data = yaml.load(
        open(helpers.get_file('rules.yaml')))
    for rule in data:
        name = rule.keys()[0]
        print "trying", name
        contains = rule[name][0]
        if validate_contains(contains):
            print "Found a match because directory contains:", (
                contains,)
            do_execute(rule[name][1])


def build_one(git_url, project_name):
    project_name_sanitized = re.sub(r'[^a-zA-Z]', '', project_name)

    tmp_dir_name = tempfile.mkdtemp(
        prefix='tmp_build_' + project_name_sanitized,
        dir='.')

    sh.git('clone', git_url, tmp_dir_name)
    with helpers.pushd(tmp_dir_name):
        execute_rules()

def build_one_main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    git_url, project_name = argv

    build_one(git_url, project_name)


def test_sample_projects_main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    data = yaml.load(
        open(helpers.get_file('test_projects.yaml')))
    for datum in data:
        name = datum.keys()[0]
        git_datum = datum[name][0]
        assert git_datum.keys() == ['git path']
        git_path = git_datum['git path']
        build_one(git_path, name)
