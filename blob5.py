import random

def rnd(a,b=0): 
  if b==0: b,a = a,0
  return random.randint(a,b-1)

#blob_tick =
class Blob5:
  def __init__(self): 
    self.duration_s = rnd(1,20) # fixme, make 1-2-4-8-16
    self.halfway = self.duration_s*0.5
    self.passed = 0 # better names?
    self.pos = (rnd(8),rnd(8))
    print('newpos', self.pos[0], self.pos[1])
    self.color1 = (rnd(255), rnd(255), rnd(255))  
  #
  def update(self, blob_tick): 
    self.passed += blob_tick
    return (self.passed >= self.duration_s)
  #
  def calc_color(self): 
    unit = 1.0-(abs(self.halfway-self.passed)/self.halfway)
    r = unit
    color=(int(r*self.color1[0]),int(r*self.color1[1]),int(r*self.color1[2]))
    return color  
  #

##############################################################
def spawn(n,blobs):
  for i in range(1,n): blobs.append(Blob5())

blobs=[Blob5(),Blob5(),Blob5()]

def updateBlobs(blob_tick):   
  global blobs
  rate=rnd(100)
  if rate<9 and len(blobs)<100: spawn(rnd(1,4), blobs)
  #print('drawStuff, len:', len(blobs))
  nextBlobs=[]
  for blob in blobs:
    done = blob.update(blob_tick)
    if not done: nextBlobs.append(blob)
  #      
  blobs = nextBlobs
  return blobs # so he can draw them.

