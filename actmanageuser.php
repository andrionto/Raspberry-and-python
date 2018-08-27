<?php
include "includes/connection.php";

$act=$_GET["act"];
$id=$_POST["id_person"];
$id_person=$_GET["id"];
$nama=$_POST["nama"];
$no_hp=$_POST["no_hp"];
$status=$_POST["status"];
if($act=="add"){
	mysql_query("insert into no_person(nama, no_hp, status) values('$nama','$no_hp','1')") or die(mysql_error());
	header('Location: kelola_user.php');
}
else if($act=="edit") {
	mysql_query("update no_person set nama='$nama', no_hp='$no_hp', status='$status' where id='$id'") or die(mysql_error());
	header('Location: kelola_user.php');
}
else if($act=="delete") {
    //print_r($id_person);die();
	mysql_query("update no_person set status = '0' where id='$id_person'") or die(mysql_error());
	header('Location: kelola_user.php');
}

?>