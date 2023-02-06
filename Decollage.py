from djitellopy import Tello

tello = Tello()
tello.connect()
batterie = tello.get_battery()
print ("La batterie est chargée à", batterie, "%")
tello.takeoff()
tello.move_forward(100)
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()
