def take_key():
  print('put the right hand to the pocket')
  print('lock the fist')
  print('take out of the hand')
  return 'KEY1'
  # pass      
  
def insert_key_to_lock(key, lock):
  print('The key %s opened the lock %s' % (key, lock))
  
def get_lock_from_door(door):
  return 'LOCK1'

def turn_key(key, clockwise=False):
  if clockwise:
    print('Key %s turned clockwise' % key)  
  else:
    print('Key %s turned anti-clockwise' % key)            
    
def open_door(key, door):
  print('go to the door')
  
  lock = get_lock_from_door(door)
  
  insert_key_to_lock(key, lock)
  print('inserted the key to the lock')
  
  turn_key(key, clockwise=False)
  print('turned the key anti-clockwise')
  
  print('push the door')