# expect_to.change
def change_before(value, from_value=None, to_value=None, by=None):
  return value

def change_after(value, from_value=None, to_value=None, by=None):
  return value

def change_check(before, after, value, from_value=None, to_value=None, by=None):
  f_present = not (from_value is None)
  t_present = not (to_value is None)
  b_present = not (by is None)
  if f_present and t_present and b_present:
    return False
  else:
    if f_present and before != from_value:   return False
    if t_present and after != to_value:      return False
    if b_present and after != before + by:   return False

  return True


# expect_to.not_change
def not_change_before(value, from_value=None, to_value=None, by=None):
  return value

def not_change_after(value, from_value=None, to_value=None, by=None):
  return value

def not_change_check(before, after, value, from_value=None, to_value=None, by=None):
  return not change_check(before, after, value, from_value=from_value, to_value=to_value, by=by)
