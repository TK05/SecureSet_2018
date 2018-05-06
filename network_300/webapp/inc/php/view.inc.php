<?php
    include_once('authcheck.inc.php');
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>View Records</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>

<h1>View Records</h1>

<p><b>View All</b> | <a href="viewpaginated.inc.php">View Paginated</a></p>

<?php
// connect to the database
include('dbh.inc.php');

// get the records from the database
if ($result = $conn->query("SELECT * FROM users ORDER BY user_id"))
{
// display records if there are records to display
if ($result->num_rows > 0)
{
// display records in a table
echo "<table border='1' cellpadding='10'>";

// set table headers
echo "<tr> <th>ID</th> <th>First Name</th> <th>Last Name</th> <th>Email</th> <th>UID</th> <th>Role</th> <th>Count</th></tr>";

while ($row = $result->fetch_object())
{
// set up a row for each record
echo "<tr>";
echo "<td>" . $row->user_id . "</td>";
echo "<td>" . $row->user_first . "</td>";
echo "<td>" . $row->user_last . "</td>";
echo "<td>" . $row->user_email . "</td>";
echo "<td>" . $row->user_uid . "</td>";
echo "<td>" . $row->user_role . "</td>";
echo "<td>" . $row->user_counter . "</td>";
echo "<td><a href='records.inc.php?user_id=" . $row->user_id . "'>Edit</a></td>";
echo "<td><a href='delete.inc.php?user_id=" . $row->user_id . "'>Delete</a></td>";
echo "</tr>";
}

echo "</table>";
}
// if there are no records in the database, display an alert message
else
{
echo "No results to display!";
}
}
// show an error if there is an issue with the database query
else
{
echo "Error: " . $conn->error;
}

// close database connection
$conn->close();

?>

<a href="records.inc.php">Add New Record</a>
</body>
</html>