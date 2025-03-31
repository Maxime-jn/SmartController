from flask import Flask, request
import RPi.GPIO as GPIO

# Configuration des broches GPIO
MOTOR_LEFT_FORWARD = 17
MOTOR_LEFT_BACKWARD = 18
MOTOR_RIGHT_FORWARD = 22
MOTOR_RIGHT_BACKWARD = 23

# Initialisation des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_LEFT_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD, GPIO.OUT)

# Fonction pour arrêter tous les moteurs
def stop_motors():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)

# Flask app
app = Flask(__name__)

@app.route('/control', methods=['GET'])
def control():
    command = request.args.get('command')
    if not command:
        return "Aucune commande reçue", 400

    # Exécution des commandes
    if command == "forward":
        GPIO.output(MOTOR_LEFT_FORWARD, GPIO.HIGH)
        GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.HIGH)
        GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
        GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)
    elif command == "backward":
        GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.HIGH)
        GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.HIGH)
        GPIO.output(MOTOR_LEFT_FORWARD, GPIO.LOW)
        GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
    elif command == "left":
        GPIO.output(MOTOR_LEFT_FORWARD, GPIO.LOW)
        GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.HIGH)
        GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
        GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)
    elif command == "right":
        GPIO.output(MOTOR_LEFT_FORWARD, GPIO.HIGH)
        GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
        GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
        GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)
    elif command == "stop":
        stop_motors()
    else:
        return "Commande inconnue", 400

    return f"Commande {command} exécutée", 200

@app.route('/shutdown', methods=['POST'])
def shutdown():
    stop_motors()
    GPIO.cleanup()
    return "Système arrêté", 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        stop_motors()
        GPIO.cleanup()
