<?php include 'koneksi.php'; ?>
<!DOCTYPE html>
<html>
<head>
	<title>Tambah Data | SimpleCRUD</title>
</head>
<body>
<h3>Tambah Data</h3>
<form action="" method="POST">
<table>
	<tr>
		<td>Nama</td>
		<td><input type="text" name="nama" placeholder="Nama"></td>
	</tr>
	<tr>
		<td>Alamat</td>
		<td><textarea name="alamat" rows="4" cols="21"></textarea></td>
	</tr>
	<tr>
		<td>Nomor Telepon</td>
		<td><input type="number" name="no_hp" placeholder="Nomor Telepon"></td>
	</tr>
	<tr>
		<td>Email</td>
		<td><input type="email" name="email" placeholder="Email"></td>
	</tr>
	<tr>
		<td colspan="2" align="right">
			<input type="reset" name="reset" value="Bersihkan">			
			<input type="submit" name="simpan" value="Simpan">		
		</td>
	</tr>
</table>
</form>
<h4><a href="index.php">Lihat Data</a></h4>
</body>
</html>
<?php 
//jika tombol simpan diklik
if (isset($_POST['simpan'])) {
	$nama = $_POST['nama'];
	$alamat = $_POST['alamat'];
	$no_hp = $_POST['no_hp'];
	$email = $_POST['email'];

	$simpan = mysql_query("INSERT INTO biodata values ('','$nama','$alamat','$no_hp','$email')")or die(mysql_error());

	if ($simpan) {
		header('location:index.php?pesan=sukses');
	}

}
?>