"""
Often people (I guess AIs might do it too) will use magic strings in their code.
The string must match in all cases or the code will fail.
This is bad! do not do this!
Make the world a better place and use constants instead!
"""


def feature_does_thing_when_on_a(other_inputs, feature_flag: str):
    if feature_flag == "this_new_feature_is_awesome":
        # Do the thing
        return True
    if feature_flag == "i_dont_know_what_to_call_this":
        # Do the thing
        return "foo"
    else:
        # Do not do the thing
        print("Feature flag is not set to 'this_new_feature_is_awesome'.")
        return False


def test_feature_does_thing_when_on_this_new_feature_is_awesome():
    assert feature_does_thing_when_on_a([], "this_new_feature_is_awesome")
    assert feature_does_thing_when_on_a([], "i_dont_know_what_to_call_this") == "foo"


def feature_does_thing_when_on_b(other_inputs, feature_flag: str):
    if feature_flag == "feature_on":
        # Do the thing
        return True
    else:
        # Do not do the thing
        print("Feature flag is not set to 'feature_on'.")
        return False


def test_feature_does_thing_when_on():
    assert feature_does_thing_when_on_b([], "feature_on")
    assert not feature_does_thing_when_on_b([], "some_other_feature")


def feature_does_thing_when_on_c(other_inputs, feature_flag: str):
    if feature_flag == "i_dont_know_what_to_call_this":
        # Do the thing
        return True
    else:
        # Do not do the thing
        print("Feature flag is not set to 'i_dont_know_what_to_call_this'.")
        return False


def test_feature_does_thing_when_on_c():
    assert feature_does_thing_when_on_c([], "i_dont_know_what_to_call_this")
    assert not feature_does_thing_when_on_c([], "some_other_feature")

