from pedal.core.feedback import CompositeFeedbackFunction
from pedal.core.commands import gently
from pedal.sandbox.commands import get_student_data


@CompositeFeedbackFunction()
def ensure_cisc108_tests(test_count, **kwargs):
    """
    Ensure that the student has not failed their own tests.
    This is for the specific ``cisc108`` library, not the general unittest
    library.
    """
    student = get_student_data()
    if 'assert_equal' not in student:
        return gently("You have not imported assert_equal from the cisc108 module.",
               label="missing_cisc108_assert_equal",
               title="Missing assert_equal", **kwargs)
    assert_equal = student['assert_equal']
    if not hasattr(assert_equal, 'student_tests'):
        return gently("The assert_equal function has been modified. Do not let it be overwritten!",
               title="overwrote_assert_equal",
               label="Overwrote assert_equal", **kwargs)
    student_tests = assert_equal.student_tests
    if student_tests.tests == 0:
        return gently("You are not unit testing the result.", title="No Student Unit Tests",
               label="no_student_tests", **kwargs)
    elif student_tests.tests < test_count:
        return gently("You have not written enough unit tests.", label="not_enough_tests",
               title="Not Enough Student Unit Tests", **kwargs)
    elif student_tests.failures > 0:
        return gently("Your unit tests are not passing.", label="failing_student_tests",
               title="Student Unit Tests Failing", **kwargs)
    return False