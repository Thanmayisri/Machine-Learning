import time
class countdown:
    def __init__(self,Time,fun):
        self.time=Time
        self.fun=fun
        self.paused=False
        self.aborted=False
    def run(self,*funs):
        # how can i modify this code to add pause, resume,  abort functionality 
        # with event system so I can add function like on and then event
        # "pause" or "resume" and pass function to it so when countdown
        # pause or resume then it will pause and execute that function please help
        while self.time>0:
            print(self.time)
            time.sleep(1)
            self.time-=1
        self.fun(*funs)
    def pause(self):
        # code to pause countdown
        def resume(self):
        # code to resume countdown
            def abort(self):
        # code to abort countdown
def samplefun(Yname,Yage):
    print('hi {a} you are {b} years old.'.format(a=Yname,b=Yage))
    count=countdown(10,samplefun)
    count.run('John Doe','30')
    time.sleep(3)
    count.pause()   # how can I make up code so when I use pause function it should pause the countdown in 7 but it doesnot pause at 7 instead of that it run 
                #pause function after countdown completes
