<?php
    session_start();

    if(!isset($_SESSION['u_role']) or $_SESSION['u_role'] != "administrator") {
        header("Location: ../../index.php?auth=deny");
        exit();
    }

?>