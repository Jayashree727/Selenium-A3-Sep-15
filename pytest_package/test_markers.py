'''
To group the testcases, we use markers
There are 2 types
    *   custom markers
    *   inbuilt markers

'''

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_reg       reg executing       PASSED
# ## test_markers.py::test_signup    signup executing    PASSED

####################################################################################

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="smoke"                -->     test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="sanity"               -->     test_login will execute
# ## pytest test_markers.py -vs -m="regression"           -->     test_logout will execute
# ## pytest test_markers.py -vs -m="smoke and sanity"     -->     None
# ## pytest test_markers.py -vs -m="smoke and regression" -->     None
# ## pytest test_markers.py -vs -m="regression and sanity"-->     None
# ## pytest test_markers.py -vs -m="smoke or sanity"      -->     test_login, test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  -->     test_reg, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="regression or sanity" -->     test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="not smoke"            -->     test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="not sanity"           -->     test_reg, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not regression"       -->     test_login, test_reg and test_signup will execute

####################################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="smoke"                -->     test_login, test_reg, test_signup will execute
# ## pytest test_markers.py -vs -m="sanity"               -->     test_login, test_logout will execute
# ## pytest test_markers.py -vs -m="regression"           -->     test_signup, test_logout will execute
# ## pytest test_markers.py -vs -m="smoke and sanity"     -->     test_login will execute
# ## pytest test_markers.py -vs -m="smoke and regression" -->     test_signup will execute
# ## pytest test_markers.py -vs -m="regression and sanity"-->     test_logout will execute
# ## pytest test_markers.py -vs -m="smoke or sanity"      -->     all 4 will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  -->     all 4 will execute
# ## pytest test_markers.py -vs -m="regression or sanity" -->     test_login, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not smoke"            -->     test_logout will execute
# ## pytest test_markers.py -vs -m="not sanity"           -->     test_reg, test_signup will execute
# ## pytest test_markers.py -vs -m="not regression"       -->     test_login, test_reg will execute

####################################################################################

@pytest.mark.sanity
class TestSample:

    def test_login(self):
        print("login executing")

    def test_reg(self):
        print("reg executing")

    def test_signup(self):
        print("signup executing")

    def test_logout(self):
        print("logout executing")

## pytest test_markers.py -vs -m="sanity"   --> All 4 will execute

# ##############################################################################################################
#
@pytest.mark.regression
class TestSample:

    @pytest.mark.sanity
    def test_login(self):
        print("login executing")

    def test_reg(self):
        print("reg executing")

    @pytest.mark.smoke
    def test_signup(self):
        print("signup executing")

    def test_logout(self):
        print("logout executing")





















































