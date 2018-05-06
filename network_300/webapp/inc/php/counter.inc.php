<?php

    session_start();

    $u_id = $_SESSION['u_id'];

    if (isset($_POST['submit'])) {
    
        include_once 'dbh.inc.php';

        //required counter variable
        $counter = $_POST['counter'];

        if (empty($counter) or !is_numeric($counter)){
            header("Location: ../../index.php?counter=error");
            exit();
        } else { 
            if ($counter <= -2147483648 or $counter >= 2147483647) {
                header("Location: ../../index.php?counter=out-of-range");
                exit();
            } else {

            //not empty or non numeric, update counter
            $sql = "UPDATE users SET user_counter='$counter' WHERE user_id='$u_id'";
            mysqli_query($conn, $sql);
            $_SESSION['u_counter'] = $counter;
            header("Location: ../../index.php?counter=updated");
            exit();
            }                
        }
    }

