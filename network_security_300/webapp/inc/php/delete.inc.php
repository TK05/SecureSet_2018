<?php

// connect to the database
include('dbh.inc.php');
include_once("authcheck.inc.php");

// confirm that the 'id' variable has been set
if (isset($_GET['user_id']) && is_numeric($_GET['user_id']))
{
// get the 'id' variable from the URL
$user_id = $_GET['user_id'];

// delete record from database
if ($stmt = $conn->prepare("DELETE FROM users WHERE user_id = ? LIMIT 1"))
{
$stmt->bind_param("i",$user_id);
$stmt->execute();
$stmt->close();
}
else
{
echo "ERROR: could not prepare SQL statement.";
}
$conn->close();

// redirect user after delete is successful
header("Location: view.inc.php");
}
else
// if the 'id' variable isn't set, redirect the user
{
header("Location: view.inc.php");
}

?>