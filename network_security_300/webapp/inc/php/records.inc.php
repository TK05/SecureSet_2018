<?php
/*
Allows the user to both create new records and edit existing records
*/

// connect to the database
include("dbh.inc.php");
include_once("authcheck.inc.php");

// creates the new/edit record form
// since this form is used multiple times in this file, I have made it a function that is easily reusable
function renderForm($u_first = '', $u_last ='', $u_email = '', $u_uid ='', $hashed_pwd='', $u_role = '', $u_counter ='', $error = '', $user_id = '')
{ ?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>
<?php if ($user_id != '') { echo "Edit Record"; } else { echo "New Record"; } ?>
</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<h1><?php if ($user_id != '') { echo "Edit Record"; } else { echo "New Record"; } ?></h1>
<?php if ($error != '') {
echo "<div style='padding:4px; border:1px solid red; color:red'>" . $error
. "</div>";
} ?>

<form action="" method="post">
<div>
<?php if ($user_id != '') { ?>
<input type="hidden" name="user_id" value="<?php echo $user_id; ?>" />
<p>ID: <?php echo $user_id; ?></p>
<?php } ?>

<strong>First Name: *<t></strong> <input type="text" name="user_first"
value="<?php echo $u_first; ?>" required/><br/>
<strong>Last Name: *</strong> <input type="text" name="user_last"
value="<?php echo $u_last; ?>" required/><br/>
<strong>Email: *</strong> <input type="email" name="user_email"
value="<?php echo $u_email; ?>" required/><br/>
<strong>Username: *</strong> <input type="text" name="user_uid"
value="<?php echo $u_uid; ?>" required/><br/>
<strong>Password: *</strong> <input type="text" name="user_pwd"
value="<?php echo $hashed_pwd; ?>" required/><br/>
<strong>Role: *</strong> <input type="text" name="user_role"
value="<?php echo $u_role; ?>" /><br/>
<strong>Counter: *</strong> <input type="text" name="user_counter"
value="<?php echo $u_counter; ?>" required/><br/>
<p>* required</p>
<input type="submit" name="submit" value="Submit" />
</div>
</form>
</body>
</html>

<?php }



/*

EDIT RECORD

*/
// if the 'id' variable is set in the URL, we know that we need to edit a record
if (isset($_GET['user_id']))
{
// if the form's submit button is clicked, we need to process the form
if (isset($_POST['submit']))
{
// make sure the 'id' in the URL is valid
if (is_numeric($_POST['user_id']))
{
// get variables from the URL/form
$user_id = $_POST['user_id'];

$sql = "SELECT 'user_pwd' FROM users WHERE user_id ='$user_id'";
$hashed_pwd = mysqli_query($conn, $sql);

$user_first = htmlentities($_POST['user_first'], ENT_QUOTES);
$user_last = htmlentities($_POST['user_last'], ENT_QUOTES);
$user_email = htmlentities($_POST['user_email'], ENT_QUOTES);
$user_uid = htmlentities($_POST['user_uid'], ENT_QUOTES);
$user_pwd = htmlentities($_POST['user_pwd'], ENT_QUOTES);
$user_role = htmlentities($_POST['user_role'], ENT_QUOTES);
$user_counter = htmlentities($_POST['user_counter'], ENT_QUOTES);

if ($hashed_pwd != $user_pwd){
    $pwd = $user_pwd;
    $user_pwd = password_hash($pwd, PASSWORD_BCRYPT);
}

// check that fields not empty
if (empty($user_first) || empty($user_last) || empty($user_email) || empty($user_uid) || empty($user_pwd) || empty($user_role))
{
// if they are empty, show an error message and display the form
$error = 'ERROR: Please fill in all required fields!';
renderForm($user_first, $user_last, $user_email, $user_uid, $user_pwd, $user_role, $user_counter, $error, $user_id);
}


else
{
$sql = "UPDATE users SET user_first = '$user_first', user_last = '$user_last', user_email = '$user_email', user_uid = '$user_uid', user_pwd = '$user_pwd', user_role = '$user_role', user_counter = '$user_counter'
WHERE user_id='$user_id'";
// if everything is fine, update the record in the database
if ($conn->query($sql) === TRUE)
{

// redirect the user once the form is updated
header("Location: view.inc.php?user=updated");
}
// show an error message if the query has an error
else
{
echo "ERROR: could not prepare SQL statement.";
}


}
}
// if the 'id' variable is not valid, show an error message
else
{
echo "Error!";
}
}
// if the form hasn't been submitted yet, get the info from the database and show the form
else
{
// make sure the 'id' value is valid
if (is_numeric($_GET['user_id']) && $_GET['user_id'] > 0)
{
// get 'id' from URL
$user_id = $_GET['user_id'];

// get the recod from the database
if($sql = $conn->prepare("SELECT * FROM users WHERE user_id=?"))
{
$sql->bind_param("i", $user_id);
$sql->execute();

$sql->bind_result($user_id, $user_first, $user_last, $user_email, $user_uid, $hashed_pwd, $user_role, $user_counter);
$sql->fetch();

// show the form
renderForm($user_first, $user_last, $user_email, $user_uid, $hashed_pwd, $user_role, $user_counter, NULL, $user_id);

$sql->close();
}
// show an error if the query has an error
else
{
echo "Error: could not prepare SQL statement";
}
}
// if the 'id' value is not valid, redirect the user back to the view.php page
else
{
header("Location: view.inc.php");
}
}
}



/*

NEW RECORD

*/
// if the 'id' variable is not set in the URL, we must be creating a new record
else
{
// if the form's submit button is clicked, we need to process the form
if (isset($_POST['submit']))
{
// get the form data
$user_first = htmlentities($_POST['user_first'], ENT_QUOTES);
$user_last = htmlentities($_POST['user_last'], ENT_QUOTES);
$user_email = htmlentities($_POST['user_email'], ENT_QUOTES);
$user_uid = htmlentities($_POST['user_uid'], ENT_QUOTES);
$user_pwd = htmlentities($_POST['user_pwd'], ENT_QUOTES);
$user_role = htmlentities($_POST['user_role'], ENT_QUOTES);
$user_counter = htmlentities($_POST['user_counter'], ENT_QUOTES);

// check that firstname and lastname are both not empty
if (empty($user_first) || empty($user_last) || empty($user_email) || empty($user_uid) || empty($user_pwd) || empty($user_role))
{
// if they are empty, show an error message and display the form
$error = 'ERROR: Please fill in all required fields!';
renderForm($user_first, $user_last, $user_email, $user_uid, $user_pwd, $user_role, $user_counter, $error, $user_id);
}
else
{
$pwd = $user_pwd;
$user_pwd = password_hash($pwd, PASSWORD_BCRYPT);
// insert the new record into the database
$sql = "INSERT INTO users (user_first, user_last, user_email, user_uid, user_pwd, user_role, user_counter) VALUES ('$user_first', '$user_last', '$user_email', '$user_uid', '$user_pwd', '$user_role', '$user_counter')";
if ($conn->query($sql) === TRUE)
{
// redirec the user
header("Location: view.inc.php?user=added");
}
// show an error if the query has an error
else
{
echo "ERROR: Could not prepare SQL statement.";
}


}

}
// if the form hasn't been submitted yet, show the form
else
{
renderForm();
}
}

// close the mysqli connection
$conn->close();
?>