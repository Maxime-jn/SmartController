<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $command = $_POST['command'];
    // Envoyer la commande à la voiture via l'accès point Wi-Fi
    $url = "http://raspberrypi.local:5000/control?command=" . $command;
    $response = file_get_contents($url);
    // Rediriger vers la page principale après l'envoi de la commande
    header('Location: index.html');
    exit();
}
?>
