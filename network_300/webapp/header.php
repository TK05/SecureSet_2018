<?php
	session_start();

?>

<!DOCTYPE html>
<html>
<head>
	<title>Tommy Kelley: %PAGE_TITLE%</title>
	<link rel="stylesheet" type="text/css" href="inc/css/style.css">
</head>
<body>

<header>
	<nav>
		<div class="main-wrapper">
			<ul>
				<li><a href="index.php">Home</a></li>
			</ul>
			<div class="nav-login">
				<?php

					if(isset($_SESSION['u_role']) && $_SESSION['u_role'] == "administrator") {
						echo '<form action="inc/php/logout.inc.php" method="POST">
							<a href="inc/php/view.inc.php" class="button">Edit</a>
							<button type="submit" name="submit">Logout</button>
							</form>';
					} else {
						if (isset($_SESSION['u_id'])) {
						echo '<form action="inc/php/logout.inc.php" method="POST">
							<button type="submit" name="submit">Logout</button>
							</form>';
					} else { 

					
						echo '<form action="inc/php/login.inc.php" method="POST">
							<input type="text" name="uid" placeholder="Username or Email" required>
							<input type="password" name="pwd" placeholder="Password" required>
							<button type="submit" name="submit">Login</button>
							</form>
							<a href="signup.php">Sign Up</a>';
					}}
				?>
							
			</div>
		</div>
	</nav>
</header>