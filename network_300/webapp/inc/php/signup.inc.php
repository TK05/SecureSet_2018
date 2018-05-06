<?php


//start on POST submit
if (isset($_POST['submit'])) {
	
	include_once 'dbh.inc.php';

	//required signup variables
	$first = $_POST['first'];
	$last = $_POST['last'];
	$email = $_POST['email'];
	$uid = $_POST['uid'];
	$pwd = $_POST['pwd'];

	//Error handlers
	//Check for empty fields
	if (empty($first) || empty($last) || empty($email) || empty($uid) || empty($pwd)) {
		
		header("Location: ../../signup.php?signup=empty");
		exit();

	} else {

		//Check if input characters are valid
		if (preg_match("/[^a-zA-Z'\ -]{1,35}/", $first) || preg_match("/[^a-zA-Z'\ -]{1,35}/", $last) || preg_match("/[^A-Za-z0-9_\-'\ .]{3,35}/", $uid) || preg_match("/[^A-Za-z0-9_!$\/\%@#]{4,45}/", $pwd)) {

			header("Location: ../../signup.php?signup=invalid");
			exit();

		} else {


			//Check if email is valid
			if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
				header("Location: ../../signup.php?signup=email");
				exit();

			} else {

				//Check valid username
				$sql = "SELECT * FROM users WHERE user_uid='$uid'";
				$result = mysqli_query($conn, $sql);
				$resultCheck = mysqli_num_rows($result);

				if ($resultCheck > 0) {
					header("Location: ../../signup.php?signup=usertaken");
				exit();

				} else {
					//all checks passed
					//Hasing the password
					$hashedPwd = password_hash($pwd, PASSWORD_BCRYPT);

					//Insert the user into the database
					$sql = "INSERT INTO users (user_first, user_last, user_email, user_uid, user_pwd) VALUES ('$first', '$last', '$email', '$uid', '$hashedPwd');";
					mysqli_query($conn, $sql);

					//auto login and session start
					session_start();
					//pull data from db (needed for u_id)
					$sqlLogin = "SELECT * FROM users WHERE user_uid='$uid'";
					$result = mysqli_query($conn, $sqlLogin);
					$row = mysqli_fetch_assoc($result);
					
					$_SESSION['u_id'] = $row['user_id'];
					$_SESSION['u_first'] = $row['user_first'];
					$_SESSION['u_last'] = $row['user_last'];
					$_SESSION['u_email'] = $row['user_email'];
					$_SESSION['u_uid'] = $row['user_uid'];
					$_SESSION['u_role'] = $row['user_role'];
					$_SESSION['u_counter'] = $row['user_counter'];
					

					header("Location: ../../index.php?signup=success");
					exit();
				}
			}
		}
	}

} else {
	header("Location: ../../signup.php");
	exit();
}