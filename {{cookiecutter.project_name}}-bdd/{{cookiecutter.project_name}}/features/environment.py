"""Hooks file."""
from behave.tag_matcher import ActiveTagMatcher
from ipdb import post_mortem


active_tag_value_provider = {
    "config_0": False
}

active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


def before_all(context):
    userdata = context.config.userdata
    context.config_0 = userdata.get('config_0', 'False')


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    if active_tag_matcher.should_exclude_with(scenario.effective_tags):
        scenario.skip(reason="DISABLED ACTIVE-TAG")


def before_tag(context, tag):
    pass


def after_step(context, step):
    if context.config.userdata.get('debug') and step.status == "failed":
        post_mortem(step.exc_traceback)


def after_tag(context, tag):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    pass
