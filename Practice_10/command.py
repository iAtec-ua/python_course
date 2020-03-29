def demo(a, b):
   print('func:',a)
   print('params:',b)

def test2(a, b):
    print("test 2", b)

class Command:
   def __init__(self, cmd, *args):
      self._cmd=cmd
      self._args=args

   def __call__(self, *args):
      return self._cmd(self._cmd, self._args+args)


cmd = Command(demo,1,2)
cmd(3)

cmd2 = Command(test2)
cmd2('hello')