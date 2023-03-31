<?php
require('connection.inc.php');
require('function.inc.php');

$name=get_safe_value($con,$_POST['name']);
$email=get_safe_value($con,$_POST['email']);
$password=get_safe_value($con,$_POST['password']);

$res = mysqli_query($con,"select * from users where email='$email'");

$check_user=mysqli_num_rows($res);
if($check_user>0){
	echo "email_present";
}else{
	mysqli_query($con,"insert into user_login(name,email,password) values('$name','$email','$password')");
	echo "insert";
}
?>