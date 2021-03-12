<?php 
$host = 'localhost';
$user = 'root'; //username database di phpmyadmin
$pass = ''; //password database di phpmyadmin defaultnya kosong => ''
$db = 'db_simplecrud'; //nama database di phpmyadmin

$connect = mysql_connect($host,$user,$pass)or die(mysql_error());

$selectdb = mysql_select_db($db);

?>