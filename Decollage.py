from djitellopy import Tello

#connexion drone tello
tello = Tello()
tello.connect()

#Test de la batterie
batterie = tello.get_battery()
print ("La batterie est chargée à", batterie, "%")

#Instructions de vol
tello.takeoff()
tello.move_forward(100)
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()
