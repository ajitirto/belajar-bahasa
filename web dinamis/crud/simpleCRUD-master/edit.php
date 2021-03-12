<?php 
include 'koneksi.php'; 
$kd_biodata = $_GET['id'];
$query = mysql_query("SELECT * FROM biodata WHERE kd_biodata='$kd_biodata'")or die(mysql_error());
$data = mysql_fetch_array($query);
?>
<!DOCTYPE html>
<html>
<head>
	<title>Edit Data | SimpleCRUD</title>
</head>
<body>
<h3>Edit Data</h3>
<form action="" method="POST">
<table>
	<tr>
		<td>Nama</td>
		<td><input type="text" name="nama" placeholder="Nama" value="<?php echo $data['nama']; ?>"></td>
	</tr>
	<tr>
		<td>Alamat</td>
		<td><textarea name="alamat" rows="4" cols="21"><?php echo $data['alamat']; ?></textarea></td>
	</tr>
	<tr>
		<td>Nomor Telepon</td>
		<td><input type="number" name="no_hp" placeholder="Nomor Telepon" value="<?php echo $data['no_hp']; ?>"></td>
	</tr>
	<tr>
		<td>Email</td>
		<td><input type="email" name="email" placeholder="Email" value="<?php echo $data['email']; ?>"></td>
	</tr>
	<tr>
		<td colspan="2" align="right">
			<input type="reset" name="reset" value="Bersihkan">			
			<input type="submit" name="update" value="Update">		
		</td>
	</tr>
</table>
</form>
<h4><a href="index.php">Lihat Data</a></h4>
</body>
</html>
<?php 
//jika tombol update di klik
if (isset($_POST['update'])) {
	$nama = $_POST['nama'];
	$alamat = $_POST['alamat'];
	$no_hp = $_POST['no_hp'];
	$email = $_POST['email'];

	$update = mysql_query("UPDATE biodata SET nama='$nama', alamat='$alamat',no_hp='$no_hp', email='$email' WHERE kd_biodata='$kd_biodata'")or die(mysql_error());

	if ($update) {
		header('location:index.php?pesan=update');
	}

}
?>