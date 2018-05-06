<?php 
    ob_start();
    include_once 'header.php';
    $buffer=ob_get_contents();
    ob_end_clean();

    $buffer=str_replace("%PAGE_TITLE%","Sign Up",$buffer);
    echo $buffer;
?>


<section class="main-container">
	<div class="main-wrapper">
		<h2>Sign Up</h2>
		<form id="register" class="signup-form" action="inc/php/signup.inc.php" method="POST">
			<input type="text" name="first" placeholder="First Name" title="Enter a valid name." pattern="[a-zA-Z'\ -]{1,35}" required />
			<input type="text" name="last" placeholder="Last Name" title="Enter a valid name." pattern="[a-zA-Z'\ -]{1,35}" required />
			<input type="email" name="email" placeholder="Email" required />
			<input type="text" name="uid" placeholder="Username (Min Length: 3)" title="Allowable characters: Uppercase, Lowercase, Numbers, -, ', . and spaces" pattern="[A-Za-z0-9_\-'\ .]{3,35}" required />

			<div class="passwordstrength">
    			<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" type="text/javascript"></script>
    			<section>
      				<input type="password" name="pwd" id="password" placeholder="Password (Min Length: 4)" minlength="4" maxlength="45" pattern="[A-Za-z0-9_!$/%@#]{4,45}" required />
  
      				<meter max="4" id="password-strength-meter"></meter>
    			</section>

    			<script src='https://cdnjs.cloudflare.com/ajax/libs/zxcvbn/4.2.0/zxcvbn.js'></script>
    			<script src="inc/js/pwdstrength.js"></script>

  			</div>

			<button type="submit" name="submit">Sign Up</button>
			
		</form>
	</div>
</section>

<?php 
	include_once 'footer.php';
?>
