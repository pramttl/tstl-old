"""
BOILERPLATE METHODS OF SUT
==========================
These are the set of methods available on each SUT by default (depending on whether they are required or not).
If t = sut.t(), then methods in this file can be used on t in the tests file which uses the harness.

Examples
--------

t.enabled()
t.actions()
"""

def enabled(self):
    """
    Returns all enabled action objects.
    """
    return filter(lambda (s, g, a): g(), self.__actions)

def features(self):
    return self.__features

def actions(self):
    """
    Returns all the action objects whether enabled or disabled.
    """
    return self.__actions

def disable(self,f):
    """
    Disable an action by name.
    """
    newActions = []
    for (name, act, guard) in self.__actions:
        if not re.match(f, name):
            newActions.append((name, act, guard))
    self.__actions = newActions

def enableAll(self):
    """
    Enable all actions.
    """
    self.__actions = self.__actions_backup

def serializable(self, step):
    return step[0]

def playable(self, name):
    return self.__names[name]

def safely(self, act):
    try:
        act()
    except:
        self.__failure = sys.exc_info()
        return False
    return True

def failure(self):
    return self.__failure

def replay(self, test, catchUncaught = False):
    self.restart()
    for (name, guard, act) in test:
        if guard():
            if catchUncaught:
                try:
                    act()
                except:
                    pass
            else:
                act()
        if not self.check():
            return False
    return True

def replayUntil(self, test, pred, catchUncaught = False):
    self.restart()
    newt = []
    if pred():
        return newt

    for (name, guard, act) in test:

        newt.append((name, guard, act))
        if guard():
            if catchUncaught:
                try:
                    act()
                except:
                    pass
            else:
                act()
        if pred():
            return newt
        if not self.check():
            return False
    return None

def failsCheck(self, test):
    try:
        return not self.replay(test, catchUncaught = True)
    except:
        return True
    return False

def fails(self, test):
    try:
        return not self.replay(test)
    except:
        return True
    return False

def logOff(self):
    self.__log = None

def logAll(self):
    self.__log = 'All'

def setLog(self, level):
    self.__log = level

def setLogAction(self, f):
    self.__logAction = f

def logPrint(self, code, text):
    print "[LOG " + str(code) + "] " + str(text)

def __candidates(self, t, n):
    candidates = []
    s = len(t) / n
    for i in xrange(0,n):
        tc = t[0:i*s]
        tc.extend(t[(i+1)*s:])
        candidates.append(tc)
    return candidates

def reduce(self, test, pred, pruneGuards = False, keepLast = True):
    """
    When a user runs his tests file like random_tests.py, etc using the SUT generate and it gives an error,
    This function uses test case minimization techniques to find the shortest sequence of actions that exhibit that bug.
    So that the user does not have to go through redundant steps to generate the bug.
    """
    try:
        test_before_reduce()
    except:
        pass
    if keepLast:
        tb = test[:-1]
        addLast = [test[-1]]
    else:
        tb = test
        addLast = []
    n = 2
    count = 0
    while True:
        count += 1
        c = self.__candidates(tb, n)
        reduced = False
        for tc in c:
            if pred(tc + addLast):
                tb = tc
                n = 2
                if pruneGuards:
                    self.restart()
                    newtb = []
                    for a in tb:
                        if a[1]():
                            newtb.append(a)
                            try:
                                a[2]()
                            except:
                                pass
                    tb = newtb
                reduced = True
                break
        if not reduced:
            if n == len(tb):
                return tb + addLast
            n = min(n*2, len(tb))
        elif len(tb) == 1:
            if pred([] + addLast):
                return ([] + addLast)
            else:
                return (tb + addLast)
