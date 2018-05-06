<?php


session_start();

//start on POST submit
if (isset($_POST['submit'])) {
	
	include 'dbh.inc.php';

	//use id and pwd
	$uid = $_POST['uid'];
	$pwd = $_POST['pwd'];

	//Error handlers
	//Check if inputs are empty
	if (empty($uid) || empty($pwd)) {
		header("Location: ../../index.php?login=empty");
		exit();

	} else {

		//not empty, select matching row from db
		$sql = "SELECT * FROM users WHERE user_uid='$uid'OR user_email ='$uid'";
		$result = mysqli_query($conn, $sql);
		$resultCheck = mysqli_num_rows($result);

		//if no matching row
		if ($resultCheck < 1) {
			header("Location: ../../index.php?login=error");
			exit();

		} else {

			if ($row = mysqli_fetch_assoc($result)) {

				//Hash password
				$hashedPwdCheck = password_verify($pwd, $row['user_pwd']);

				//check for correct password
				if ($hashedPwdCheck != $pwd) {
					header("Location: ../../index.php?login=error");
					exit();

					//log in the user if everything matches
				} elseif ($hashedPwdCheck == $pwd) {
					$_SESSION['u_id'] = $row['user_id'];
					$_SESSION['u_first'] = $row['user_first'];
					$_SESSION['u_last'] = $row['user_last'];
					$_SESSION['u_email'] = $row['user_email'];
					$_SESSION['u_uid'] = $row['user_uid'];
					$_SESSION['u_role'] = $row['user_role'];
					$_SESSION['u_counter'] = $row['user_counter'];
					header("Location: ../../index.php?login=success");
					exit();

				}
			}
		}
	} 

} else {
		header("Location: ../../index.php?login=error");
		exit();
}

