<?php 
	ob_start();
	include_once 'header.php';
	$buffer=ob_get_contents();
    ob_end_clean();

    $buffer=str_replace("%PAGE_TITLE%","Index",$buffer);
    echo $buffer;
?>

<section class="main-container">
	<div class="main-wrapper">
		<?php 

			if(isset($_SESSION['u_id'])) {
				echo "<h2>Hello ".$_SESSION['u_uid']."</h2><br>";
				echo "<center><br><br>";
				echo'<form action="inc/php/counter.inc.php" method="POST">
                    	<input type="text" name="counter" value='.$_SESSION['u_counter'].' required>
                        <button type="submit" name="submit">Update</button>
                    </form>';
				echo "</center>";

			} else {
				echo "<h2>Please Login to Access Counter </h2>";
			}

			
		?>
	</div>
</section>

<?php 
	include_once 'footer.php';
?>
